import os
import urllib.parse

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'}

def is_image(filename):
    return any(filename.lower().endswith(ext) for ext in IMAGE_EXTS)

def create_gallery_readme_for_dir(folder_path):
    # Only files in this folder
    images = [f for f in os.listdir(folder_path) 
              if os.path.isfile(os.path.join(folder_path, f)) and is_image(f)]
    if not images:
        return
    # Markdown content
    md_lines = ["# Image Gallery\n"]
    for img in images:
        md_img_path = urllib.parse.quote(img)
        md_lines.append(f"![{img}](./{md_img_path})")
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write('\n\n'.join(md_lines))
    print(f"Wrote {len(images)} images to {readme_path}")

def process_all_subdirs(root_dir):
    for entry in os.listdir(root_dir):
        entry_path = os.path.join(root_dir, entry)
        if os.path.isdir(entry_path):
            create_gallery_readme_for_dir(entry_path)

if __name__ == "__main__":
    # Set your target directory here (usually ".")
    target_dir = "."
    process_all_subdirs(target_dir)

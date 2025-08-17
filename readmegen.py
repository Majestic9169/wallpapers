import os
from urllib.parse import quote

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'}

def is_image(filename):
    return any(filename.lower().endswith(ext) for ext in IMAGE_EXTS)

def create_gallery_readme_for_dir(folder_path):
    images = [f for f in os.listdir(folder_path)
              if os.path.isfile(os.path.join(folder_path, f)) and is_image(f)]
    if not images:
        return False
    md_lines = ["# Image Gallery\n"]
    for img in images:
        md_img_path = quote(img)
        md_lines.append(f"![{img}](./{md_img_path})")
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write('\n\n'.join(md_lines))
    print(f"Wrote {len(images)} images to {readme_path}")
    return True

def process_all_subdirs(root_dir):
    galleries = [] # (relative_path, title)
    for entry in os.listdir(root_dir):
        entry_path = os.path.join(root_dir, entry)
        if os.path.isdir(entry_path):
            made_gallery = create_gallery_readme_for_dir(entry_path)
            if made_gallery:
                galleries.append((entry, entry.replace("_", " ").title()))
    return galleries

def create_master_readme(root_dir, galleries):
    md_lines = ["# Image Gallery Index\n"]
    md_lines.append("Browse image galleries in subfolders:\n")
    for folder, title in galleries:
        folder_path = quote(folder)
        md_lines.append(f"- [{title}]({folder_path}/README.md)")
    readme_path = os.path.join(root_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(md_lines))
    print(f"Wrote master gallery README with {len(galleries)} links to {readme_path}")

if __name__ == "__main__":
    target_dir = "."
    galleries = process_all_subdirs(target_dir)
    create_master_readme(target_dir, galleries)

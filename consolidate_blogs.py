import os
import shutil

ROOT_DIR = "."
BLOG_DIR = "blogs"
BACKUP_DIR = "backup"
EXTENSIONS_TO_UPDATE = {".html", ".js", ".css"}
DRY_RUN = False  # Set to True to preview actions, False to apply changes

def ensure_backup_dir():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def backup_file(filepath):
    relative_path = os.path.relpath(filepath, ROOT_DIR)
    backup_path = os.path.join(BACKUP_DIR, relative_path)
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    shutil.copy2(filepath, backup_path)
    print(f"[BACKUP] {filepath} -> {backup_path}")

def find_duplicates_by_name():
    root_files = [f for f in os.listdir(ROOT_DIR) if f.startswith("blog_") and f.endswith(".html")]
    blog_files = [f for f in os.listdir(BLOG_DIR) if f.startswith("blog_") and f.endswith(".html")]

    print("Root blog files:", root_files)
    print("Blogs folder files:", blog_files)

    duplicates = [f for f in root_files if f in blog_files]
    return duplicates

def delete_duplicates(duplicates):
    for file in duplicates:
        file_path = os.path.join(ROOT_DIR, file)
        if DRY_RUN:
            print(f"[DRY RUN] Would delete: {file_path}")
        else:
            backup_file(file_path)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def update_references():
    for foldername, _, filenames in os.walk(ROOT_DIR):
        if BACKUP_DIR in foldername or "node_modules" in foldername:
            continue
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext in EXTENSIONS_TO_UPDATE:
                filepath = os.path.join(foldername, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()

                new_content = content.replace('href="blog_', 'href="blogs/blog_')\
                                     .replace("href='blog_", "href='blogs/blog_")\
                                     .replace('src="blog_', 'src="blogs/blog_')\
                                     .replace("src='blog_", "src='blogs/blog_")

                if content != new_content:
                    if DRY_RUN:
                        print(f"[DRY RUN] Would update references in: {filepath}")
                    else:
                        backup_file(filepath)
                        with open(filepath, "w", encoding="utf-8") as file:
                            file.write(new_content)
                        print(f"Updated references in: {filepath}")

def main():
    ensure_backup_dir()
    print("Finding duplicate blog files by filename...")
    duplicates = find_duplicates_by_name()
    if not duplicates:
        print("No duplicates found.")
    else:
        print(f"Duplicate filenames: {duplicates}")
        delete_duplicates(duplicates)

    print("Scanning and updating references...")
    update_references()
    print("Done.")

if __name__ == "__main__":
    main()

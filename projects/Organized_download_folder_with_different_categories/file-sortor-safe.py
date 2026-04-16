import os
import shutil
import sys

# Safe path for testing
target_dir = "test_env/downloads"
output_dir = "test_env/sorting"

if not os.path.exists(target_dir):
    print(f"Error: {target_dir} not found.")
    sys.exit(1)

os.chdir(target_dir)

# Ensure output directory exists
if not os.path.exists("../sorting"):
    os.makedirs("../sorting")

files = os.listdir()

extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}

def sorting(file):
    for key, exts in extentions.items():
        for ext in exts:
            if file.lower().endswith(ext):
                return key
    return None

for file in files:
    if os.path.isdir(file):
        continue
        
    dist = sorting(file)
    if not dist:
        dist = "others"
        
    # Create subfolder if it doesn't exist
    final_dist_path = os.path.join("..", "sorting", dist)
    if not os.path.exists(final_dist_path):
        os.makedirs(final_dist_path)
        
    try:
        shutil.move(file, os.path.join(final_dist_path, file))
        print(f"Moved {file} to {dist}")
    except Exception as e:
        print(f"Error moving {file}: {e}")

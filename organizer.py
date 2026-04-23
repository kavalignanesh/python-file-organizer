import os
import shutil

path = os.getcwd()
files = os.listdir(path)

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

for file in files:
    for folder, extensions in file_types.items():
        if any(file.endswith(ext) for ext in extensions):
            os.makedirs(folder, exist_ok=True)

            destination = os.path.join(folder, file)

            if not os.path.exists(destination):
                shutil.move(file, destination)
                print(f"Moved {file} → {folder}")
            else:
                print(f"Skipped duplicate: {file}")

print("Smart automation complete 🚀")


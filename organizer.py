import os
import shutil

path = os.getcwd()
files = os.listdir(path)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        os.makedirs("Images", exist_ok=True)
        shutil.move(file, "Images/" + file)

    elif file.endswith(".pdf") or file.endswith(".docx"):
        os.makedirs("Documents", exist_ok=True)
        shutil.move(file, "Documents/" + file)

    elif file.endswith(".mp4"):
        os.makedirs("Videos", exist_ok=True)
        shutil.move(file, "Videos/" + file)

print("Files organized successfully!")

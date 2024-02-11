import os
import shutil
import sys

def organize_files(source_path):
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        if os.path.isfile(file_path):
            move_file(file_path)

def move_file(file_path):
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    destination_dir = None

    if file_extension in (".txt", ".csv", ".tsv", ".json", ".xml", ".md"):
        destination_dir = r"D:\Downloads\Text Files"
    elif file_extension in (".pdf"):
        destination_dir = r"D:\Downloads\PDF Files"
    elif file_extension in (".docx", ".xlsx", ".pptx", ".ppt", ".doc"):
        destination_dir = r"D:\Downloads\Office Files"
    elif file_extension in (".zip", ".rar"):
        destination_dir = r"D:\Downloads\Compressed Files"
    elif file_extension in (".jpg", ".jpeg", ".png", ".gif", ".raw", ".webp", ".dng"):
        destination_dir = r"D:\Downloads\Pictures"
    elif file_extension in (".java", ".class", ".py", ".c", ".cpp", ".html", ".sql"):
        destination_dir = r"D:\Downloads\Code"
    elif file_extension in (".exe"):
        destination_dir = r"D:\Downloads\Executable Files"
    elif file_extension in (".mp3", ".wav"):
        destination_dir = r"D:\Downloads\Music"
    elif file_extension in (".mp4", ".mov", ".mxf"):
        destination_dir = r"D:\Downloads\Videos"

    if destination_dir:
        new_path = os.path.join(destination_dir, file_name)
        shutil.move(file_path, new_path)
        print(f"Moved '{file_name}' to '{destination_dir}'")

if __name__ == '__main__':
    source_path = sys.argv[1] if len(sys.argv) > 1 else '.'  # Use provided path or current directory

    organize_files(source_path)
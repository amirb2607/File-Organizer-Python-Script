#Created by Amir Badrudeen to Organize Downloaded Files!
#
# How to call script:
# python3 "scriptName" "Path/To/Watch" "File_Name_Of_Log_File"
# Change the directories of the destination_dir's for the collection of file types 
# to however you see fit.

import sys
import time
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, PatternMatchingEventHandler, LoggingEventHandler 

class Handler(PatternMatchingEventHandler):
    # Storing our logs to a file.
    # File Name is determined by the 2nd argument passed.
    logging.basicConfig(filename = sys.argv[2], filemode= 'a', level=logging.INFO,
        format = '%(asctime)s | %(process)d | %(message)s',
                         datefmt='%m-%d-%Y %I:%M:%S %p')
    
    def __init__(self) -> None:
        PatternMatchingEventHandler.__init__(self, patterns=["*"], 
        ignore_directories=True, case_sensitive=False)
    
    def on_created(self, event):
        logging.info(f"A file was created in: {event.src_path}")
        if os.path.isfile(event.src_path):
            file_name = os.path.basename(event.src_path)
            file_extension = os.path.splitext(file_name)[1].lower()
            destination_dir = None
            # Each extension has a directory that it will be moved to.
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
                #To minimize the risk of corrupted files, the script will sleep for 25 seconds before it moves the file.
                time.sleep(25)
                shutil.move(event.src_path, new_path)
                logging.info(f"Moved '{file_name}' to '{destination_dir}'")

    def on_modified(self, event):
        logging.info(f"A file was modified in: {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"A file was deleted in: {event.src_path}")

if __name__ == '__main__':
    # Path will be argument 1,
    # If no arguments are provided it will monitor the root folder.
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
    
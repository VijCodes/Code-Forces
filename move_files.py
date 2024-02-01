#!/opt/homebrew/bin/python3

import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def move_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):  # Check if it's a file
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} to {dest_path}")

class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            return
        # Run the move_files function when a modification is detected
        move_files(event.src_path, destination_folder)

# Path to the folder you want to monitor
watched_folder = "/Users/vijaykatta/Documents/Code Forces"
# Path to the destination folder
destination_folder = "/Users/vijaykatta/Documents/Old Code"

# Immediately move files when the script starts
move_files(watched_folder, destination_folder)
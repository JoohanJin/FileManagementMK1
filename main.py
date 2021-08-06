from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import sys
import json
import time

# implementation of a subclass of watchdog.events.FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # each file in the directory == "folder_to_track"
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            # use os to rename the file in the directory 
            os.rename(src, new_destination)

folder_to_track = "/home/joshep/Downloads"
folder_destination = "/home/joshep/Desktop/testFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10) # time delay for 0.01 sec
except KeyboardInterrupt:
    observer.stop()
observer.join()

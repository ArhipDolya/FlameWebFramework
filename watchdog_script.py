import os
import sys
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartOnCodeChange(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename

    def on_modified(self, event):
        if event.src_path.endswith(self.filename):
            print('Code change detected in', self.filename, 'Restarting server...')
            subprocess.run([sys.executable, self.filename])  # Use sys.executable to run the script

if __name__ == '__main__':
    filename_to_watch = 'manage.py'
    event_handler = RestartOnCodeChange(filename_to_watch)
    observer = Observer()
    current_directory = os.path.dirname(os.path.realpath(__file__))
    observer.schedule(event_handler, current_directory, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

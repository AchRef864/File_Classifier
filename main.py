import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

extension_types = {
    'images': ['jpg', 'png', 'webp'],
    'documents': ['pdf', 'docx', 'xlsx', 'csv', 'txt'],
    'archives': ['zip', 'tar', 'rar'],
    'executables': ['exe', 'msi', 'jar', 'whl'],
    'configuration': ['ini'],
    'torrent': ['torrent']
}

def get_category(extension):
    for category, ext_list in extension_types.items():
        if extension in ext_list:
            return category
    return 'others'

class Watcher:
    DIRECTORY_TO_WATCH = "C:/Users/rahal/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if not event.is_directory:
            print(f"File {event.src_path} has been created")
            # Trigger your Python script or function here
            os.system('classify_file.py')

if __name__ == '__main__':
    w = Watcher()
    w.run()
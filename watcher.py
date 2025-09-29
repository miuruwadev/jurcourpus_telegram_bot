import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys

class Watcher(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_bot()

    def start_bot(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, "bot.py"])

    def on_modified(self, event):
        if (event.is_directory or
            not event.src_path.endswith(".py") or
            "__pycache__" in event.src_path or
            event.src_path.endswith("watch.py")):
            return
        print(f"Detected modification in {event.src_path}, restarting bot...")
        self.start_bot()

def main():
    path = "."
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
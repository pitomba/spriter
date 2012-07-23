from gen_image import Sprite
from watchdog.observers import Observer
import ConfigParser
import os
import time

config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
img_dir = config.get("dirs", "img")

class Handler:
    def dispatch(self, event):
        if not event.is_directory:
            path = os.path.dirname(event.src_path)
            files = [os.path.join(path,arq) for arq in os.listdir(path)]
            sprite = Sprite(files)
            sprite.gen_sprite()

if __name__ == "__main__":
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=img_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
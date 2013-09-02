from sprite import Sprite
from watchdog.observers import Observer
import ConfigParser
import os
import time

config = ConfigParser.ConfigParser()

config_file = os.path.abspath(os.curdir) + "/config.cfg"
config.readfp(open(config_file, "r"))

img_dir = config.get("dirs", "img_dir")
css_dir = config.get("dirs", "css_dir")
sprite_dir = config.get("dirs", "sprite_dir")
class_name = config.get("dirs", "class_name")


class Handler(object):
    def dispatch(self, event):
        if event.is_directory:
            return False

        path = os.path.dirname(event.src_path)
        files = [os.path.join(path, arq) for arq in os.listdir(path)]
        sprite = Sprite(files, css_path=css_dir, sprite_path=sprite_dir,
                        class_name=class_name)
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

# -*- coding: utf-8 -*-
from optparse import OptionParser
from spriter import VERSION
from spriter.sprite import Sprite
from watchdog.observers import Observer
import imghdr
import ConfigParser
import os
import sys
import time


global img_dir
global css_dir
global sprite_dir
global class_name


class Handler(object):
    def dispatch(self, event):
        if event.is_directory:
            return False

        path = os.path.dirname(event.src_path)

        print("Image {0} {1}").format(os.path.basename(event.src_path),
                                      event.event_type)
        files = []
        for arg in os.listdir(path):
            j = os.path.join(path, arg)
            if imghdr.what(j) is not None:
                files.append(j)

        sprite = Sprite(files,
                        css_path=css_dir,
                        sprite_path=sprite_dir,
                        class_name=class_name)

        sprite.gen_sprite()

if __name__ == "__main__":
    argv = sys.argv[1:]

    parser = OptionParser(version=VERSION)
    parser.add_option("-c", "--config", dest="config",
                      help="Path do config.cfg",
                      metavar="CONFIG")

    (options, args) = parser.parse_args()

    if not options.config:
        print 'You must provide a config.cfg file.'
        sys.exit(2)

    config = ConfigParser.ConfigParser()
    config.readfp(open(options.config, "r"))
    img_dir = config.get("dirs", "img_dir")
    css_dir = config.get("dirs", "css_dir")
    sprite_dir = config.get("dirs", "sprite_dir")
    class_name = config.get("dirs", "class_name")

    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=img_dir, recursive=True)

    print("Listening to {0}...").format(img_dir)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

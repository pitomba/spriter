# -*- coding: utf-8 -*-
from spriter.sprite import Sprite

import os

SPRITE_PATH = os.getcwd() + "/demo/sprite/"
CSS_PATH = os.getcwd() + "/demo/css/"
IMAGE_PATH = os.getcwd() + "/demo/img/"


def gen_sprite():
    css = ""
    path = None

    files = []

    #get images absolut paths
    for (_, _, filenames) in os.walk(IMAGE_PATH):
        files.extend(map(lambda x: "{0}{1}".format(IMAGE_PATH, x), filenames))
        break

    if files != []:
        sprite = Sprite(files,
                        #path where sprite will be generated
                        sprite_path=SPRITE_PATH,

                        #optional
                        sprite_url="http://pitomba.org/static/demo/sprite.png",

                        #optional, defines where css will be saved
                        css_path=CSS_PATH,

                        #optional, defines a namespace for your sprite
                        class_name="demo")

        import pdb;pdb.set_trace()
        css = sprite.do_write_css()
        path = sprite.do_write_image()
    return (css, path)

if __name__ == "__main__":
    print("Starting spriter demo")
    css, path = gen_sprite()
    print("Done! Verify {0}").format(SPRITE_PATH)

# -*- coding: utf-8 -*-
from spriter.sprite import Sprite

import os

SPRITE_PATH = os.getcwd() + "/demo/sprite/"
CSS_PATH = os.getcwd() + "/demo/css/"
IMAGE_PATH = os.getcwd() + "/demo/img/"


def gen_sprite():
    css = ""
    image = ""
    files = []

    #get images absolut paths
    for (_, _, filenames) in os.walk(IMAGE_PATH):
        files.extend(map(lambda x: "{0}{1}".format(IMAGE_PATH, x), filenames))
        break

    if files != []:
        #instantiate Sprite class
        sprite = Sprite(files,
                        #path where sprite will be generated
                        sprite_path=SPRITE_PATH,

                        #optional
                        sprite_name="demo.png",

                        #optional
                        sprite_url="http://pitomba.org/static/demo/",

                        #optional, defines where css will be saved
                        css_path=CSS_PATH,

                        #optional, defines a namespace for your sprite
                        class_name="demo")

        #write css file and return OS path
        css = sprite.do_write_css()

        #write sprite file and return OS path
        image = sprite.do_write_image()

        #if you just want the CSS file content simply use:
        #sprite.get_css()
        #this will return a string that can be used anyway you want to.
    return (css, image)

if __name__ == "__main__":
    print("Starting spriter demo")
    css, path = gen_sprite()
    print("Done! Verify {0}").format(SPRITE_PATH)

# -*- coding: utf-8 -*-
from StringIO import StringIO
import os
import re
import urllib
from unicodedata import normalize
from PIL import Image


__all__ = ["FileImage", "URLImage"]

word = re.compile(r'[^\w]')


class CantAccessURLImage(Exception):
    pass


def class_name_function(path):
    """The general rule of css's class name is:
    case insensitive; not preceded by number and, in general, ascii letters.
    The filename will be transformed in lowercas;
    all non-ascii letters will be change to empty string;
    all non letter or non number will be change to '-';
    started by letter s to avoid numbers-only filenames"""
    base_name = os.path.basename(path).split(".")[0]
    path = "s%s" % word.sub("-", base_name.lower().encode("ascii", "ignore"))
    return path


class BaseImage(object):

    def __init__(self, path, class_name=None,
                 class_name_function=class_name_function):
        if class_name is None:
            self.class_name = class_name_function(path)
        else:
            self.class_name = class_name
        self.sprite_coordinate_x = None
        self.sprite_coordinate_y = None

    def _set_image(self, img):
        self.raw = Image.open(img)
        self.width = self.raw.size[0]
        self.height = self.raw.size[1]


class URLImage(BaseImage):
    def __init__(self, url, default_url="", class_name=None,
                 class_name_function=class_name_function):
        super(URLImage, self).__init__(url, class_name, class_name_function)
        img = self.__opener(url, default_url)
        self._set_image(img)

    def __opener(self, url, default):
        img = urllib.urlopen(url)
        if img.code != 200:
            #presumed default is http: 200!
            img = urllib.urlopen(default)
        return StringIO(img.read())


class FileImage(BaseImage):
    def __init__(self, path, default_path="", class_name=None,
                 class_name_function=class_name_function):
        super(FileImage, self).__init__(path, class_name, class_name_function)
        if (not os.path.exists(path)) and (default_path != ""):
            path = default_path
        self._set_image(path)

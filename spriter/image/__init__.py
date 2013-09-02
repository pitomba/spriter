from PIL import Image
from StringIO import StringIO
import os
import urllib

__all__ = ["FileImage", "URLImage"]


class CantAccessURLImage(Exception):
    pass


class BaseImage(object):
    def __init__(self, path):
        self.class_name = os.path.basename(path).split(".")[0]
        self.sprite_coordinate_x = None
        self.sprite_coordinate_y = None

    def _set_image(self, img):
        self.raw = Image.open(img)
        self.width = self.raw.size[0]
        self.height = self.raw.size[1]


class URLImage(BaseImage):
    def __init__(self, url, default_url=""):
        super(URLImage, self).__init__(url)
        img = self.__opener(url, default_url)
        self._set_image(img)

    def __opener(self, url, default):
        img = urllib.urlopen(url)
        if img.code != 200:
            #presumed default is http: 200!
            img = urllib.urlopen(default)
        return StringIO(img.read())


class FileImage(BaseImage):
    def __init__(self, path, default_path=""):
        super(FileImage, self).__init__(path)
        if (not os.path.exists(path)) and (default_path != ""):
            path = default_path
        self._set_image(path)

from PIL import Image
import os

__all__ = ["file_image"]


class BaseImage(object):
    def __init__(self, path):
        self.class_name = os.path.basename(path).split(".")[0]
        self.sprite_coordinate_x = None
        self.sprite_coordinate_y = None


# class URLImage(BaseImage):
#     pass


class FileImage(BaseImage):
    def __init__(self, path, default_path=""):
        super(FileImage, self).__init__(path)
        if (not os.path.exists(path)) and (default_path != ""):
            path = default_path
        self.raw = Image.open(path)
        self.width = self.raw.size[0]
        self.height = self.raw.size[1]

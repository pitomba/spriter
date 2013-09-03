from PIL import Image
from image import FileImage
from spriter.image import URLImage
import os


class DefaultImageDoesNotExist(Exception):
    message = "The default image path must be exist. Not found in: "

    def __init__(self, path):
        super(DefaultImageDoesNotExist, self).__init__(
                  self.message)
        self.message = self.message + path


class Sprite(object):

    __CSS_TEMPLATE = ".{CLASSES}{{background:url(\"{ROOT_PATH}{SPRITE_NAME}\") 0 0 no-repeat}}"
    __CSS_CLASS_TEMPLATE = ".{CLASSES}.{CLASS_NAME}{{background-position: {POSITION_X}px {POSITION_Y}px}}"

    def __init__(self,
                 paths=[],
                 urls_paths=[],
                 sprite_path=None,
                 sprite_name=None,
                 sprite_url=None,
                 image_format="RGBA",
                 css_path="",
                 class_name="sprite",
                 css_name="sprite.css",
                 optimize=False,
                 default_path="",
                 default_url=""):

        self.images = []
        self.height = 0
        self.width = 0

        if default_path is not None and default_path is not "":
            if not isinstance(default_path, str):
                raise TypeError(
                            "The default image path must be a string instance")
            if not os.path.exists(default_path):
                raise DefaultImageDoesNotExist(default_path)

        for path in paths:
            img = FileImage(path, default_path)
            self.images.append(img)

        for path in urls_paths:
            img = URLImage(path, default_url)
            self.images.append(img)

        if sprite_name:
            self.sprite_name = sprite_name
        else:
            self.sprite_name = "sprite.png"

        self.optimize = optimize

        self.image_format = image_format
        self.css_name = css_name
        self.class_name = class_name
        self.sprite_path = sprite_path or os.getcwd() + "/"
        self.css_path = css_path or os.getcwd() + "/"
        self._set_sprite_image_dimension()

        if sprite_url:
            self.sprite_url = sprite_url
        else:
            self.sprite_url = self.sprite_path

    def _set_sprite_image_dimension(self):

        for image in self.images:

            image.sprite_coordinate_y = 0

            if self.height < image.height:
                self.height = image.height

            image.sprite_coordinate_x = -(self.width)
            self.width += image.width

    def get_css(self):
        """given the sprite's css string"""
        css_line = []

        for image in self.images:
            css_line.append(
                    self.__CSS_CLASS_TEMPLATE.format(CLASSES=self.class_name,
                                                CLASS_NAME=image.class_name,
                                        POSITION_X=image.sprite_coordinate_x,
                                        POSITION_Y=image.sprite_coordinate_y))

        base = self.__CSS_TEMPLATE.format(CLASSES=self.class_name,
                                       ROOT_PATH=self.sprite_url,
                                       SPRITE_NAME=self.sprite_name)
        css_line.insert(0, base)
        css = "".join(css_line)
        return css

    def do_write_css(self):
        """Write css's file"""
        if not os.path.exists(self.css_path):
            os.makedirs(self.css_path)

        path = os.path.join(self.css_path, self.css_name)

        css_f = open(path, "w")
        css = self.get_css()
        css_f.write(css)
        css_f.close()
        return path

    def gen_image(self):

        self.image = Image.new(self.image_format, (self.width, self.height))
        width = 0

        for image in self.images:
            self.image.paste(image.raw,
                             (width, 0))
            width += image.width

    def do_write_image(self):
        """Write sprite file"""
        if not hasattr(self, "image"):
            self.gen_image()
        if not os.path.exists(self.sprite_path):
            os.makedirs(self.sprite_path)
        path = os.path.join(self.sprite_path, self.sprite_name)
        if self.optimize:
            self.image.save(path, "PNG", optimize=1)
        else:
            self.image.save(path, "PNG")
        return path

    def gen_sprite(self):
        css_path = self.do_write_css()
        image_path = self.do_write_image()
        return (css_path, image_path)

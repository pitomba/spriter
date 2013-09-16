import os

from PIL import Image

from spriter.image import FileImage, URLImage, class_name_function


class DefaultImageDoesNotExist(Exception):
    message = "The default image path must be exist. Not found in: "

    def __init__(self, path):
        super(DefaultImageDoesNotExist, self).__init__(
                  self.message)
        self.message = self.message + path


class Sprite(object):

    __CSS_TEMPLATE = ".{self.class_name}{{background:url(\"{self.sprite_url}{self.sprite_name}\") 0 0 no-repeat}}"
    __CSS_CLASS_TEMPLATE = ".{self.class_name}.{image.class_name}{{background-position: {image.sprite_coordinate_x}px {image.sprite_coordinate_y}px}}"

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
                 optimize=True,
                 default_path="",
                 default_url="",
                 class_name_function=class_name_function):

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
            img = FileImage(path, default_path,
                            class_name_function=class_name_function)
            self.images.append(img)

        for path in urls_paths:
            img = URLImage(path, default_url,
                           class_name_function=class_name_function)
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
        css_line = [self.__CSS_TEMPLATE.format(self=self)]

        for image in self.images:
            css_line.append(
                    self.__CSS_CLASS_TEMPLATE.format(self=self, image=image))
        css = "".join(css_line)
        return css

    def do_write_css(self):
        """Write css's file"""
        if not os.path.exists(self.css_path):
            os.makedirs(self.css_path)

        path = os.path.join(self.css_path, self.css_name)
        with open(path, "w") as css_f:
            css = self.get_css()
            css_f.write(css)
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
            self.image.save(path, "PNG",
                            optimize=1, compress_level=2, compress_type=1)
        else:
            self.image.save(path, "PNG")
        return path

    def gen_sprite(self):
        css_path = self.do_write_css()
        image_path = self.do_write_image()
        return (css_path, image_path)

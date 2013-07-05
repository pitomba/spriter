from PIL import Image
import os


class URLImage(object):
    pass


class FileImage(object):

    def __init__(self, path):
        self.raw = Image.open(path)
        self.width = self.raw.size[0]
        self.height = self.raw.size[1]
        self.sprite_coordinate_x = None
        self.sprite_coordinate_y = None
        self.class_name = os.path.basename(path).split(".")[0]


class Sprite(object):

    __CSS_TEMPLATE = ".{CLASSES}{{background:url(\"{ROOT_PATH}{SPRITE_NAME}\") 0 0 no-repeat}}"
    __CSS_CLASS_TEMPLATE = ".{CLASSES}.{CLASS_NAME}{{background-position: {POSITION_X}px {POSITION_Y}px}}"

    def __init__(self, paths, sprite_path=None,
                 sprite_name=None,
                 sprite_url=None, image_format="RGBA", css_path="",
                 class_name="sprite", css_name="sprite.css"):

        self.images = []
        self.height = 0
        self.width = 0
        for path in paths:
            self.images.append(FileImage(path))
        if  sprite_path:
            self.sprite_path = sprite_path
        else:
            self.sprite_path = os.getcwd()
        if sprite_url:
            self.sprite_url = sprite_url
        else:
            self.sprite_url = self.sprite_path
        if sprite_name:
            self.sprite_name = sprite_name
        else:
            self.sprite_name = "sprite.png"

        self.image_format = image_format
        self.css_name = css_name
        self.class_name = class_name
        self.css_path = css_path
        self._set_sprite_image_demision()

    def _set_sprite_image_demision(self):

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

    def do_write_css(self, css_name=None):
        """Write css's file"""
        if not css_name:
            css_name = self.css_name

        path = os.path.abspath(os.curdir) + "/" + self.css_path + css_name

        css_f = open(path, "w")
        css = self.get_css()
        css_f.write(css)
        css_f.close()

    def gen_image(self):

        self.image = Image.new("RGBA", (self.width, self.height))
        width = 0

        for image in self.images:

            self.image.paste(image.raw,
                             (width, 0))
            width += image.width

    def do_write_image(self):
        if not hasattr(self, "image"):
            self.gen_image()
        if not os.path.exists(self.sprite_path):
            os.makedirs(self.sprite_path)
        path = os.path.join(self.sprite_path, self.sprite_name)
        self.image.save(path, "PNG", options='optimize')
        return path

    def gen_sprite(self):
        self.do_write_css()
        self.do_write_image()

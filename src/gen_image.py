import Image
import os


class URLImage:
    pass

class FileImage:
    def __init__(self, path):
        self.raw = Image.open(path)
        self.width = self.raw.size[0]
        self.height = self.raw.size[1]
        self.sprite_coordinate_x = None
        self.sprite_coordinate_y = None
        self.class_name = os.path.basename(path).split(".")[0]

class Sprite:
    __CSS_TEMPLATE = "{CLASSES}{{background:url({ROOT_PATH}/{SPRITE_NAME}) 0 0 no-repeat}}"
    __CSS_CLASS_TEMPLATE = ".{CLASS_NAME}{{background-position: {POSITION_X}px {POSITION_Y}px }}"

    def __init__(self, paths, sprite_path=None, 
                 sprite_name=None, image_format="RGBA", css_path="", css_name="sprite.css"):
        self.images = []
        self.height = 0
        self.width = 0
        for path in paths:
            self.images.append(FileImage(path))
        print len(self.images)
        if  sprite_path:
            self.sprite_path = sprite_path
        else:
            self.sprite_path = os.getcwd()
        
        if sprite_name:
            self.sprite_name = sprite_name
        else:
            self.sprite_name = "sprite.png"

        self.image_format = image_format
        self.css_name = css_name
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
        
        classes = []
        css_line = []
        for image in self.images:
            classes.append("."+image.class_name)
            css_line.append(self.__CSS_CLASS_TEMPLATE.format(CLASS_NAME=image.class_name,
                                                           POSITION_X=image.sprite_coordinate_x,
                                                           POSITION_Y=image.sprite_coordinate_y))
        base = self.__CSS_TEMPLATE.format(CLASSES=",".join(classes),
                                       ROOT_PATH=self.sprite_path,
                                       SPRITE_NAME=self.sprite_name)

        css_line.insert(0, base)
        css = "\n".join(css_line)
        return css

    def do_write_css(self, css_name=None):
        if not css_name:
            css_name = self.css_name
        path = self.css_path+css_name
        css_f = open(path,"w")
        css = self.get_css()
        css_f.write(css)
        css_f.close()

    def gen_image(self):
        self.image = Image.new("RGBA", (self.width, self.height))
        width = 0
        for image in self.images:
            
            self.image.paste(image.raw,
                             (width, 0))#,image.raw)
            width += image.width

    def do_write_image(self):
        if not hasattr(self, "image"):
            self.gen_image()
        path = os.path.join(self.sprite_path, self.sprite_name)
        self.image.save(path, "PNG", options='optimize')

    def gen_sprite(self):
        self.do_write_css()
        self.do_write_image()

from PIL import Image
from spriter.sprite import Sprite
import os
import unittest


class TestSprite(unittest.TestCase):
    def test_demission_sprite(self):
        """Tests width and height after gen sprite"""
        paths = ["tests/sad.png", "tests/happy.png"]
        sprite = Sprite(paths)
        #128 each image has 64 px
        assert sprite.width == 64 + 64
        assert sprite.height == 64

    def test_css_format(self):
        paths = ["tests/sad.png", "tests/happy.png"]
        sprite = Sprite(paths)
        css = sprite.get_css()
        self.assertEquals(css, ".sprite{background:url(%ssprite.png) 0 0 no-repeat}\n.sad{background-position: 0px 0px }\n.happy{background-position: -64px 0px }" % os.getcwd())

    def test_do_write_css(self):
        paths = ["tests/sad.png", "tests/happy.png"]
        sprite = Sprite(paths, sprite_path=os.getcwd() + "/tests/")
        sprite.do_write_css()
        assert os.path.exists(os.getcwd() + "/tests/sprite.css")

    def test_gen_image(self):
        paths = ["tests/sad.png", "tests/happy.png"]
        sprite = Sprite(paths, sprite_path=os.getcwd() + "/tests/")
        sprite.gen_image()
        assert sprite.image.size[0] == 128
        assert sprite.image.size[1] == 64
        assert sprite.image.size[0] == sprite.width
        assert sprite.image.size[1] == sprite.height
        assert sprite.image.mode == "RGBA"

    def test_do_write_image(self):

        paths = ["tests/sad.png", "tests/happy.png"]
        sprite = Sprite(paths, sprite_path=os.getcwd() + "/tests/")
        path = sprite.do_write_image()
        sprite.gen_image()
        self.assertTrue(os.path.exists(path))

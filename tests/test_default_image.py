from spriter.sprite import Sprite, DefaultImageDoesNotExist
from PIL import Image
import os
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.paths = ["tests/fixtures/sad.png"]

    def test_error_when_default_path_is_not_a_str(self):
        self.assertRaises(TypeError,
                          Sprite,
                          self.paths, default_path=1)

    def test_error_when_default_path_is_set_but_does_not_exists(self):
        self.assertRaises(DefaultImageDoesNotExist,
                          Sprite,
                          self.paths, default_path="ERROR")

    def test_write_a_default_image_when_some_path_does_not_exist(self):
        self.paths.append("tests/ERROR.png")
        default_path = os.getcwd() + "/tests/fixtures/default.png"
        sprite = Sprite(self.paths, default_path=default_path)
        sprite.gen_image()
        path = sprite.do_write_image()
        css = sprite.get_css()
        self.assertIn(".sprite.serror", css)
        sprite_img = Image.open(path)
        compare = Image.open(os.getcwd() + "/tests/fixtures/with_default.png")
        #This assert the default image is in the sprite
        self.assertEquals(sprite_img.histogram(), compare.histogram())

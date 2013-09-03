from PIL import Image
from spriter.sprite import Sprite
from tests import Openned
import mock
import os
import unittest


class TestSprite(unittest.TestCase):

    def setUp(self):
        self.paths = ["tests/fixtures/sad.png", "tests/fixtures/happy.png"]

    def test_content_url_sprite(self):
        sprite = Sprite(self.paths, sprite_url="http://localhost:8000/")
        css = sprite.get_css()
        self.assertIn("http://localhost:8000/sprite.png", css)

    def test_demission_sprite(self):
        """Tests width and height after gen sprite"""
        sprite = Sprite(self.paths)

        #128 each image has 64 px
        assert sprite.width == 64 + 64
        assert sprite.height == 64

    def test_css_format(self):
        sprite = Sprite(self.paths)
        css = sprite.get_css()
        self.assertEquals(css,
                          ".sprite{background:url(\"%s/sprite.png\") 0 0 no-repeat}.sprite.sad{background-position: 0px 0px}.sprite.happy{background-position: -64px 0px}" % os.getcwd())

    def test_do_write_css(self):
        """Tests whether a CSS can be correctly written or not"""
        sprite = Sprite(self.paths,
                        sprite_path=os.getcwd() + "/tests/",
                        css_path=os.getcwd() + "/tests/")

        sprite.do_write_css()
        assert os.path.exists(os.getcwd() + "/tests/sprite.css")

    def test_gen_image(self):
        sprite = Sprite(self.paths, sprite_path=os.getcwd() + "/tests/")
        sprite.gen_image()
        assert sprite.image.size[0] == 128
        assert sprite.image.size[1] == 64
        assert sprite.image.size[0] == sprite.width
        assert sprite.image.size[1] == sprite.height
        assert sprite.image.mode == "RGBA"

    def test_do_write_image(self):
        sprite = Sprite(self.paths, sprite_path=os.getcwd() + "/tests/")
        path = sprite.do_write_image()
        sprite.gen_image()
        self.assertTrue(os.path.exists(path))

    def test_image_from_urls(self):
        with mock.patch("urllib.urlopen") as mck:
            mck.return_value = Openned("http://pitomba.org/happy.png")
            mck.return_value = Openned("http://pitomba.org/sad.png")
            sprite = Sprite(paths=[],
                            urls_paths=["http://pitomba.org/happy.png",
                                        "http://pitomba.org/sad.png"],
                            sprite_name="sprite_url.png")
            path = sprite.do_write_image()
            self.assertIn("sprite_url.png", path)
            compare = Image.open(os.getcwd() + "/tests/fixtures/sprite_url.png")
            self.assertEquals(compare.histogram(), sprite.image.histogram())

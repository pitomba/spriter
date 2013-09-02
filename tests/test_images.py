from PIL import Image
from spriter.image import URLImage
from tests import Openned
import mock
import unittest


class TestImage(unittest.TestCase):

    def test_simple_url_get_base(self):
        with mock.patch("urllib.urlopen") as mck:
            mck.return_value = Openned("http://pitomba.org/happy.png")
            img = URLImage("http://pitomba.org/happy.png")
            img_pil = Image.open("tests/fixtures/happy.png")
            self.assertEquals(img_pil.histogram(), img.raw.histogram())

    def test_simple_url_get_base_with_default(self):
        with mock.patch("urllib.urlopen") as mck:
            mck.return_value = Openned("http://pitomba.org/happy.png")
            mck.return_value.code = 404
            img = URLImage("404", default_url="http://pitomba.org/happy.png")
            img_pil = Image.open("tests/fixtures/happy.png")
            self.assertEquals(img_pil.histogram(), img.raw.histogram())

import unittest

from spriter.image import BaseImage


class TestBaseImage(unittest.TestCase):

    def test_default_class_name(self):
        image = BaseImage("a.png", "abc")
        self.assertEquals(image.class_name, "abc")

    def test_class_name_based_in_path(self):
        image = BaseImage("a.png")
        self.assertEquals(image.class_name, "a")

    def test_class_name_function_override(self):
        func = lambda x: "s" + x
        image = BaseImage("a.png", class_name_function=func)
        self.assertEquals(image.class_name, "sa.png")

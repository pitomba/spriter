'''
Created on 02/09/2013

@author: romulo.jales
'''
from spriter.sprite import Sprite
import os
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.paths = ["tests/fixtures/sad.png", "tests/fixtures/happy.png"]

    def test_gen_image_when_optimize_arg_is_not_passed(self):
        sprite = Sprite(self.paths)
        path = sprite.do_write_image()
        self.assertTrue(os.path.exists(path))

    def test_gen_image_when_optimize_arg_is_passed(self):
        sprite = Sprite(self.paths, optimize=True)
        path = sprite.do_write_image()
        self.assertTrue(os.path.exists(path))

    def test_image_optimizated_is_small_than_not_optimizated(self):
        sprite_op = Sprite(self.paths, optimize=True, sprite_name="op.png")
        sprite_nop = Sprite(self.paths, optimize=False, sprite_name="nop.png")
        path_op = sprite_op.do_write_image()
        path_nop = sprite_nop.do_write_image()
        self.assertLess(os.stat(path_op).st_size, os.stat(path_nop).st_size)

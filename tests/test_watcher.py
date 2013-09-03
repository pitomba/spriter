import os
import unittest
from spriter import spriter_watcher

global img_dir
global css_dir
global sprite_dir
global class_name


class FakeEvent():

    def __init__(self):
        self.is_directory = False
        self.src_path = os.path.join(os.path.abspath(os.curdir), 'tests',
                                     'fixtures', 'happy.png')
        self.event_type = "created"


class HandlerTestCase(unittest.TestCase):
    img_dir = "."
    css_dir = "."
    sprite_dir = "."
    class_name = "test"

    def setUp(self):
        self.event = FakeEvent()

    def test_dont_handle_when_event_is_directory(self):
        self.event.is_directory = True
        handler = spriter_watcher.Handler()

        response = handler.dispatch(self.event)
        self.assertEqual(response, False)

#     def test_handle_when_event_is_not_directory(self):
#         handler = spriter_watcher.Handler()
#         handler.dispatch(self.event)

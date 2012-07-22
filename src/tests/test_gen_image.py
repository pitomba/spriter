from gen_image import Sprite
import os

def test_demission_sprite():
    """Tests width and height after gen sprite"""
    paths = ["tests/sad.png", "tests/happy.png"]
    sprite = Sprite(paths)
    assert sprite.width == 64 + 64 #128 each image has 64 px
    assert sprite.height == 64
    
def test_css_format():
    paths = ["tests/sad.png", "tests/happy.png"]
    sprite = Sprite(paths)
    css = sprite.get_css()

    assert css == ".sad,.happy{background:url(/Users/romulo.jales/pessoal/spriter/src/sprite.png) 0 0 no-repeat}\n"+\
                   ".sad{background-position: 0px 0px }\n"+\
                   ".happy{background-position: -64px 0px }"

def test_do_write_css():
    paths = ["tests/sad.png", "tests/happy.png"]
    sprite = Sprite(paths, sprite_path=os.getcwd()+"/tests/")
    sprite.do_write_css()
    assert os.path.exists(os.getcwd()+"/tests/sprite.css")
    
def test_gen_image():
    paths = ["tests/sad.png", "tests/happy.png"]
    sprite = Sprite(paths, sprite_path=os.getcwd()+"/tests/")
    sprite.gen_image()
    assert sprite.image.size[0] == 128
    assert sprite.image.size[1] == 64
    assert sprite.image.size[0] == sprite.width
    assert sprite.image.size[1] == sprite.height
    assert sprite.image.mode == "RGBA"

def test_do_write_image():
    paths = ["tests/sad.png", "tests/happy.png"]
    sprite = Sprite(paths, sprite_path=os.getcwd()+"/tests/")
    sprite.gen_image()
    sprite.do_write_image()
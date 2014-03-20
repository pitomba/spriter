[![Travis CI](https://travis-ci.org/pitomba/spriter.png?branch=master)](https://travis-ci.org/pitomba/spriter)
[![Coverage Status](https://coveralls.io/repos/pitomba/spriter/badge.png)](https://coveralls.io/r/pitomba/spriter)
[![Requirements Status](https://requires.io/github/pitomba/spriter/requirements.png?branch=master)](https://requires.io/github/pitomba/spriter/requirements/?branch=master)
[![PyPI version](https://pypip.in/v/spriter/badge.png)](https://pypip.in/v/spriter/)
[![Downloads number](https://pypip.in/d/spriter/badge.png)](https://crate.io/packages/spriter/)

Spriter
--------

Spriter is a simple and flexible dynamic sprite generator for CSS, using Python. It can process CSS both
synchronous and asynchronous as it provides classes to be used in your python code and also a watcher
that listens to your filesystem and changes CSS and sprite as soon as a static is changed.


Installation
------------

**Automatic installation**::

    pip install spriter

Spriter is listed in [PyPI](http://pypi.python.org/pypi/spriter/) and
can be installed with ``pip`` or ``easy_install``.

**Manual installation**: Download the latest source from [PyPI](http://pypi.python.org/pypi/spriter/).

    tar xvzf spriter-$VERSION.tar.gz
    cd spriter-$VERSION
    sudo python setup.py install

Spriter source code is [hosted on GitHub](https://github.com/pitomba/spriter).


Usage
------------

It's really simple to use pitomba sprites generator.
Imagine you have 3 images files at your home's directory: ~/1.png,  ~/2.png, ~/3.png. Then open the python interpreter

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"])
css_path, image_path = sprt.gen_sprite()
print css_path
print image_path
```

This sprite was generated using the Spriter

![Alt mosaico](http://s.glbimg.com/es/ge/f/mosaico/mosaico/1/201309031416/sprite.png)

A more detailed explanation.
The source distribution includes demo applications that are not present
when Spriter is installed via pip or easy_install, so you may wish to download the source tarball.



* [Demo](http://pitomba.org/demo)

Flags used by demo app are provided by [FAMFAMFAM](http://www.famfamfam.com/lab/icons/flags/)

Documentation
-------------
Spriter attributes:

* paths=[], List of images locals paths
* urls_paths=[], List of urls images
* sprite_path=None, where the sprite will save the sprite's file. If none, will be save at CWD
* sprite_name=None, The name of sprite's file. If none, the name is sprite.png
* sprite_url=None, the sprite url to write in css, if none will consider sprite_path
* image_format="RGBA", To save as png
* css_path="", where the sprite will save the sprite's file. If "", will be save at CWD
* class_name="sprite", The name of base css class
* css_name="sprite.css", The name of css file
* optimize=True, Save image optimized 
* default_path="", Path for the image that will be used as faultback when Spriter can't find an image
* default_url="", Same as default_path but instead of Path use an URL
* class_name_function=class_name_function, function to generate a css item class name.
* image_extension="PNG", extension to save sprite image

Sprites works with paths and urls_paths at same time. So if you have a local image and an Internet image the Spriter will merge the files onto a sprite file.

class_name_function:

    """The general rule of css's class name is:
    case insensitive; not preceded by number and, in general, ascii letters.
    The filename will be transformed in lowercas;
    all non-ascii letters will be change to empty string;
    all non letter or non number will be change to '-';
    started by letter s to avoid numbers-only filenames"""
    
So, The css class name of an image named "123.png" will be: "s123"


Spriter functions:

* get_css(), get only the css string.
* get_css_base64(), get the css string with base64 image encode.
* get_base64_str(), get the base64 sprite's img.
* do_write_css(), Do write the CSS' file at css_path with class_name.
* gen_image(), Get sprite image's bytes.
* do_write_image(), Do write IMAGE's file at css_path with class_name.
* gen_sprite(), Do write both IMAGE and CSS files.


* [pitomba.org](http://pitomba.org)

WebP Support
------------

First, be sure complete [google's webp install instructions](https://developers.google.com/speed/webp/docs/precompiled) before proceed. 

Then, (re-)install Pillow's library.

To save an sprite as webp be sure the image_extension property equals to WEBP, and the sprite's name with webp extension (sprite.webp).

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"], image_extension="WEBP", sprite_name="sprite.webp")
sprt.do_write_image()
```

Since webp's format is not fully supported by all major web browser use it when you have absolute certain that your clients have support to this extension.

Visit [Can I Use's website](http://caniuse.com/webp) to follow up the evolution of support 


Base64 Support
------------

Since version 1.2 is possibile to generate base64 sprite, i.e without generate the sprite files and put directly in css's string (file).

To get the base64 strings:

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"])
image_str = sprt.get_base64_str()
```

To get the css's string with base64 sprite string:

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"])
css_str = sprt.get_css_base64()
```

If you want generate the css file:

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"])
css_path = sprt.do_write_css(is_base64=True)
```

Or

```python
from spriter import Spriter
sprt = Spriter(["~/1.png", "~/2.png", "~/3.png"])
css_path, image_path = sprt.gen_sprite(is_base64=True)
```

the last script don't write the image file (i.e, image path is None).

Contribute
----------

Get touch via github. Don't be shy, open an issue or mail us. We speak PT_BR too. ;) 

Or following up [How to contribute](http://pitomba.org/contribute)



License
-------------

* [MIT License](http://pitomba.mit-license.org/)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/pitomba/spriter/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


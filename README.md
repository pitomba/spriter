[![Travis CI](https://travis-ci.org/pitomba/spriter.png)](https://travis-ci.org/pitomba/spriter)
[![Coverage Status](https://coveralls.io/repos/pitomba/spriter/badge.png)](https://coveralls.io/r/pitomba/spriter)
[![PyPI version](https://pypip.in/v/spriter/badge.png)](https://pypip.in/v/spriter/)
[![Downloads number](https://pypip.in/d/spriter/badge.png)](https://crate.io/packages/spriter/)

Pitomba
--------

Pitomba is a simple and flexible sprite generator for CSS, using Python. It can process CSS both
synchronous and asynchronous as it provides classes to be used in your python code and also a watcher
that listens to your filesystem and changes CSS and sprite as soon as a static is changed.


Installation
------------

**Automatic installation**::

    pip install spriter

Pitomba is listed in [PyPI](http://pypi.python.org/pypi/spriter/) and
can be installed with ``pip`` or ``easy_install``.

**Manual installation**: Download the latest source from [PyPI](http://pypi.python.org/pypi/spriter/).

    tar xvzf spriter-$VERSION.tar.gz
    cd spriter-$VERSION
    sudo python setup.py install

Pitomba source code is [hosted on GitHub](https://github.com/pitomba/spriter).


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

A more detailed explanation.
The source distribution includes demo applications that are not present
when Pitomba is installed via pip or easy_install, so you may wish to download the source tarball.



* [Demo](http://pitomba.org/demo)

Flags used by demo app are provided by [FAMFAMFAM](http://www.famfamfam.com/lab/icons/flags/)


Contribute
----------

* [How to contribute](http://pitomba.org/contribute)


Documentation
-------------

* [pitomba.org](http://pitomba.org)


License
-------------

* [MIT License](http://pitomba.mit-license.org/)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from spriter import VERSION

setup(
    name=u'spriter',
    version=VERSION,
    description=u"Pitomba's sprite generator",
    long_description=u"""
                        Pitomba provides simple and flexible optimized sprite
                        generator for CSS, using Python.

                        Pitomba can process CSS both synchronous and asynchronous as it
                        provides classes to be used in your python code and
                        also a watcher that listens to your filesystem and
                        changes CSS and sprite as soon as a static is changed.

                        """,
    keywords='pitomba sprite css images generator',
    author=u'Romulo Jales',
    author_email='romulo@romulojales.com',
    url='http://pitomba.org',
    download_url='https://github.com/pitomba/pitomba',
    license='Apache License 2.0',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python'],
    packages=find_packages(),
    package_dir={"spriter": "spriter"},
    include_package_data=True,
    scripts=['spriter/spriter_watcher.py'],
    test_suite="tests"
)

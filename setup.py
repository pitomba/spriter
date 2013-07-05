# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from spriter import VERSION

setup(
    name=u'spriter',
    version=VERSION,
    description=u"Pitomba's sprite generato",
    long_description=u"""Pitomba provides simple and flexible sprite generator
                        for CSS, using Python.""",
    keywords='pitomba sprite css images',
    author=u'Romulo Jales',
    author_email='romulo@romulojales.com',
    url='https://github.com/pitomba/pitomba',
    license='Public',
    classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'],
    packages=find_packages(),
    package_dir={"spriter": "spriter"},
    include_package_data=True,
    test_suite="tests"
)

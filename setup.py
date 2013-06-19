# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name=u'spriter',
    version="0.0.1",
    description=u"Pitomba's sprite generato",
    long_description=u"""Pitomba provides simple and flexible sprite generator for CSS, using Python.""",
    keywords='pitomba sprite css images',
    author=u'Rômulo Jales',
    author_email='romulo@romulojales.com',
    url='https://github.com/pitomba/pitomba',
    license='Public',
    classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'],
    packages=find_packages(),
    package_dir={"spriter": "src"},
    include_package_data=True,
    test_suite="tests"
)

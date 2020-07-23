import os
import sys
from setuptools import setup


if os.path.exists('README.rst'):
    if sys.version_info > (3,):
        description_long = open('README.rst', encoding="utf-8").read()
    else:
        description_long = open('README.rst').read()
else:
    description_long = """
Python utilities for manipulating EXIF data directly via libexif
"""

setup(
    name='libexif-cffi',
    version="0.1",
    description="exif manipulation utilities",
    description_long=description_long,
    author="Gerald Thibault",
    url="http://github.com/dieselmachine/libexif-cffi.git",
    author_email="dieselmachine@gmail.com",
    license='MIT',
    packages=['libexif'],
    package_data={'libexif': ['libexif.cdef']},
    setup_requires=['cffi >= 1.0'],
    install_requires=['cffi >= 1.0'],
    cffi_modules=["libexif/libexif_build.py:ffi"]
)
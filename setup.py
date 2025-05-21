from setuptools import setup


setup(
    cffi_modules=["libexif/libexif_build.py:ffibuilder"]
)

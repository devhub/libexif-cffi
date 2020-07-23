import os

from cffi import FFI


with open(os.path.join(os.path.dirname(__file__), 'libexif.cdef')) as fp:
    CDEF = fp.read()


SOURCE = """
#include "libexif/exif-data.h"
"""


ffi = FFI()
ffi.set_source("_libexif", SOURCE, libraries=['exif'])
ffi.cdef(CDEF)


if __name__ == '__main__':
    ffi.compile()

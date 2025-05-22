import os

from cffi import FFI
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path


ffibuilder = FFI()

PROJECT_PATH = Path(__file__).parent.parent
PACKAGE_ABS_PATH = Path(__file__).parent
PACKAGE_REL_PATH = PACKAGE_ABS_PATH.relative_to(PROJECT_PATH)

with open(PACKAGE_ABS_PATH / 'c-src' / 'libexif.c', 'r') as f:
    ffibuilder.set_source(
        module_name="_libexif",
        source=f.read(),
        libraries=["exif"],
    )

with open(PACKAGE_ABS_PATH / 'c-src' / 'cdef.c', 'r') as f:
    ffibuilder.cdef(f.read())


if __name__ == '__main__':
    ffibuilder.compile()

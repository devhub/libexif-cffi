from _libexif import ffi, lib


def fromstring(s):
    """
    creates an ExifData cdata obj from a string
    """
    in_data_len = len(s)
    in_data_p = ffi.new("unsigned char[]", in_data_len)
    inbuf = ffi.buffer(in_data_p, in_data_len)
    inbuf[:] = s
    return lib.exif_data_new_from_data(s, len(s))


def tostring(exifdata):
    """
    converts an ExifData cdata obj to a string
    """
    out_data_p = ffi.new("char[]", exifdata.size)
    out_data = ffi.new("unsigned char **", out_data_p)
    ds = ffi.new("unsigned int *")
    lib.exif_data_save_data(exifdata, out_data, ds)
    tmp = ffi.unpack(out_data, 1)[0]
    return ffi.buffer(tmp, ds[0])[:]


def filter_tags(exifdata, func):
    """
    filters exif ifd entries based on the result of func(entry.tag)
    """
    for i in range(5):
        ifd = exifdata.ifd[i]
        for j in range(ifd.count-1, -1, -1):
            entry = ifd.entries[j]
            if not func(entry.tag):
                lib.exif_content_remove_entry(ifd, entry)


def filter_exif(data, func):
    exif = fromstring(data)
    filter_tags(exif, func)
    return tostring(exif)

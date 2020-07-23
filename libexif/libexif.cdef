typedef struct {
    unsigned int tag;
    unsigned int format;
    unsigned long components;
    unsigned char *data;
    unsigned int size;
    ...;
} ExifEntry;

typedef struct {
    ExifEntry **entries;
    unsigned int count;
    ...;
} ExifContent;

typedef struct {
    ExifContent *ifd[5];
    unsigned char *data;
    unsigned int size;
    ...;
} ExifData;

ExifData    *exif_data_new_from_data (const unsigned char *data,
                                      unsigned int size);
void        exif_content_remove_entry (ExifContent *c, ExifEntry *e);
void        exif_data_save_data (ExifData *data, unsigned char **d,
                                 unsigned int *ds);
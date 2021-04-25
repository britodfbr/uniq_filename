
import pathlib
import string
from functools import partial


def uniq_fn(filename, letters: bool = False):
    """ mine """
    filename = pathlib.Path(filename)
    n = (x for x in range(int(1e100)))
    g = (x for x in string.ascii_lowercase)
    suffix = ''.join(filename.suffixes)
    stem = filename.stem.split('.')[0]
    if filename.exists():
        while True:
            fn = filename.with_name(f"{stem}_{next(g)}").with_suffix(suffix) \
            if letters else \
            filename.with_name(f"{stem}_{next(n):03d}").with_suffix(suffix)
            if not fn.is_file():
                return fn
    return filename

uniq_filename = partial(uniq_fn, letters=True)


def uniq_filename0(filename):
    """ mine """
    filename = pathlib.Path(filename)
    g = (x for x in string.ascii_lowercase)
    suffix = ''.join(filename.suffixes)
    stem = filename.stem.split('.')[0]
    if filename.exists():
        while True:
            fn = filename.with_name(f"{stem}{next(g)}").with_suffix(suffix)
            if not fn.is_file():
                return fn
    return filename


def uniq_file(self, src, dst):
    """ mine """
    src = pathlib.Path(src)
    dst = pathlib.Path(dst)
    g = (x for x in string.ascii_lowercase)
    if dst.exists() and not src.samefile(dst):
        while True:
            suffix = ''.join(src.suffixes)
            stem = src.stem.split('.')[0]
            newdst = dst.with_stem(f"{stem}{next(g)}").with_suffix(suffix)
            if not newdst.exists():
                return newdst
    return dst


def unique_path(directory, name_pattern):
    """ https://realpython.com/python-pathlib/ """
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path



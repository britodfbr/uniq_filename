import uniq_filename
import pathlib
from platform import python_version


if python_version() < '3.8.0':
    print('Py 3.8+')
    exit(1)

path = uniq_filename.unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')
pathlib.Path(path).touch()

file = uniq_filename.uniq_filename('file.txt')
file.touch()

f2 = uniq_filename.uniq_fn('file.txt', False)
f2.touch()

f3 = uniq_filename.uniq_fn('file.txt', True)
f3.touch()


if __name__ == "__main__":
    print(path)

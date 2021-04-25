import uniq_filename
import pathlib
from platform import python_version


if python_version() < '3.8.0':
    print('Py 3.8+')
    exit(1)

path = uniq_filename.unique_path(pathlib.Path.cwd(), 'dir_output/test{:03d}.txt')
path.parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(path).touch()

file = uniq_filename.uniq_filename('dir_output/test.txt')
file.touch()

f2 = uniq_filename.uniq_fn('dir_output/test.txt', False)
f2.touch()

f3 = uniq_filename.uniq_fn('dir_output/test.txt', True)
f3.touch()


if __name__ == "__main__":
    print(path)
    # [x.unlink() for x in pathlib.Path().glob('*.txt')]

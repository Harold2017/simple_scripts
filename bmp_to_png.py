from PIL import Image
import sys


def bmp_to_png(filenames):
    for filename in filenames:
        img = Image.open(filename)
        img.save(filename.split('.')[0] + '.png', 'png')


if __name__ == '__main__':
    script = sys.argv.pop(0)

    if len(sys.argv) < 2:
        print('Usage: python {} <duration> <path to images separated by space>'.format(script))
        sys.exit(1)

    filenames = sys.argv

    bmp_to_png(filenames)

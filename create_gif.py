# script from DSK @IdiotInside
import sys
import sys
import datetime
import imageio


VALID_EXTENSITIONS = ('png', 'jpg')


def creat_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'GIF-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == '__main__':
    script = sys.argv.pop(0)

    if len(sys.argv) < 2:
        print('Usage: python {} <duration> <path to images separated by space>'.format(script))
        sys.exit(1)

    duration = float(sys.argv.pop(0))
    filenames = sys.argv

    if not all(f.lower().endswith(VALID_EXTENSITIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    creat_gif(filenames, duration)

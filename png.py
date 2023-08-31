from os import listdir, remove, replace, path
from numpy import array, any
from PIL import Image


def get_png_list(path_dir: str):
    return [i for i in listdir(path_dir) if i.endswith('.png')]


def is_trans(direction: str):

    image = Image.open(direction)

    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    img_array = array(image)
    alpha_channel = img_array[:, :, 3]

    return any(alpha_channel < 255)


def create_trans(direction: str):

    if path.exists(fr'{direction}\png'):
        direction = fr'{direction}\png' if len(get_png_list(fr'{direction}\png')) != 0 else direction
    else:
        direction = direction

    image_list = get_png_list(direction)

    if len(image_list) != 0:

        print('The process has started...\n')

        for img in image_list:

            if '_trans' not in img and is_trans(fr'{direction}\{img}'):

                image = Image.open(fr'{direction}\{img}')
                image = image.convert('RGBA')
                pixels = image.load()
                width, height = image.size

                for y in range(height):
                    for x in range(width):

                        r, g, b, a = pixels[x, y]
                        pixels[x, y] = (a, a, a, a)

                if '_color.png' in img:
                    img = img.replace('_color.png', '_trans.png')
                else:
                    img = img.replace('.png', '_trans.png')

                image.save(fr'{direction}\{img}')
                print(f'[CREATE]: {img}')

        input('\nProcess completed!')

    else:
        input('There are no png files in the current directory!')

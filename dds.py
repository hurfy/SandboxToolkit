from os import listdir, remove, replace, path, mkdir
from PIL import Image


def get_dds_list(dir_path: str):
    return [i for i in listdir(dir_path) if i.endswith('.dds')]


def dds_refactoring(direction: str):

    dds_list = get_dds_list(direction)

    if len(dds_list) != 0:

        low = input('Remove low(y/n)? ')
        print('The process has started...')

        for img in dds_list:

            if low == 'y':

                if f'MIP_{img}' in dds_list or img.endswith('_low.dss') \
                        or img.startswith('low') or img.startswith('MIP_low'):

                    print(f'[REMOVE]: {img}')
                    remove(fr'{direction}\{img}')
            else:

                if f'MIP_{img}' in dds_list:
                    print(f'[REMOVE]: {img}')
                    remove(fr'{direction}\{img}')

        dds_list = get_dds_list(direction)

        for img in dds_list:
            if 'MIP_' in img:
                print(f'[RENAME]: {img}')
                replace(fr'{direction}\{img}', fr'{direction}\{img.replace("MIP_", "")}')

        input('\nProcess completed!')

    else:
        input('There are no dds files in the current directory!')


def dds_to_png(direction: str):

    dds_list = get_dds_list(direction)

    if len(dds_list) != 0:

        print('The process has started...')

        if not path.exists(fr'{direction}\png'):
            mkdir(fr'{direction}\png')

        for img in dds_list:

            if img.replace('dds', 'png') not in listdir(fr'{direction}\png'):

                dds_image = Image.open(fr'{direction}\{img}')
                dds_image = dds_image.convert('RGBA')
                dds_image.save(fr'{direction}\png\{img.replace("dds", "png")}', 'PNG')

                print(f'[CONVERT]: {img.replace("dds", "png")}')

        input('\nProcess completed!')

    else:
        input('There are no dds files in the current directory!')

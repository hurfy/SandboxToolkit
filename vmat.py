from os import mkdir, getcwd, listdir, path
from pprint import pprint

PATH = r'/'


def get_default_img_list():

    return [i for i in listdir(PATH) if '_color' in i]


def get_all_img_list():

    return [i for i in listdir(PATH)]


def get_img_types():

    img_maps_list = []

    for img in get_default_img_list():

        img = img.replace("_color.png", "")
        maps_list = get_all_img_list()

        img_types = {
            'color':     f'{img}_color.png',
            'mask':      f'{img}_mask.png'      if f'{img}_mask.png'      in maps_list else '',
            'normal':    f'{img}_normal.png'    if f'{img}_normal.png'    in maps_list else '',
            'rough':     f'{img}_rough.png'     if f'{img}_rough.png'     in maps_list else '',
            'metal':     f'{img}_metal.png'     if f'{img}_metal.png'     in maps_list else '',
            'ao':        f'{img}_ao.png'        if f'{img}_ao.png'        in maps_list else '',
            'blend':     f'{img}_blend.png'     if f'{img}_blend.png'     in maps_list else '',
            'height':    f'{img}_height.png'    if f'{img}_height.png'    in maps_list else '',
            'trans':     f'{img}_trans.png'     if f'{img}_trans.png'     in maps_list else '',
            'selfillum': f'{img}_selfillum.png' if f'{img}_selfillum.png' in maps_list else '',
            'freedom':   f'{img}_freedom.png'   if f'{img}_freedom.png'   in maps_list else ''
        }

        img_maps_list.append(img_types)

    return img_maps_list


def create_material():
    pass

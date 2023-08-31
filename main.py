from os import getcwd, listdir, system
from consolemenu import SelectionMenu
from art import text2art

from dds import dds_refactoring, dds_to_png
from png import create_trans


PATH = getcwd()


def create_menu(items: list):
    art = text2art("SBOX\n")
    menu = SelectionMenu(items, title=f'{art}Hello world!          hurfy', show_exit_option=False)
    menu.show()

    system('cls')

    return menu.selected_option


def main():
    main_menu_dict = {0: 'create_vmat',
                      1: create_trans,
                      2: dds_to_png,
                      3: 'generate_sbox',
                      4: dds_refactoring}

    main_menu = create_menu(['Create vmat',
                             'Create trans',
                             'Convert DDS to PNG',
                             'Create s&box textures [M2 Only]',
                             'DDS Refactoring       [M2 Only]'])

    main_menu_choice = main_menu_dict.get(main_menu)
    main_menu_choice(PATH)


if __name__ == '__main__':
    main()

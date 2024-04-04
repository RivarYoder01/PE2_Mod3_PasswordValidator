#!/user.bin.env python3

"""


GitHub URL: https://github.com/RivarYoder01/PE2_Mod3_PasswordValidator
"""

__author__ = 'Rivar Yoder | Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/8/2024'
__status__ = 'Development'

from password_validator import PasswordValidator


def display_errors(pw):
    """

    :param pw:
    :return:
    """
    print(f'{pw} is an invalid password')

    for e in pw.get_errors():
        print(e)


def default_validator():
    """

    :return:
    """

    passwords = ("AAaa11!!", "Abb12!!", "AAb12!", "AAbb1", "AAbb12!", "b!")
    pv = PasswordValidator()

    for p in passwords:
        if pv.is_valid(p):
            print(f'{pv} is a valid password')
        else:
            display_errors(pv)

        print()


if __name__ == '__main__':
    default_validator

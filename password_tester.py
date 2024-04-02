#!/user.bin.env python3

"""


GitHub URL: https://github.com/RivarYoder01/PE2_Mod3_PasswordValidator
"""

__author__ = 'Rivar Yoder | Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/8/2024'
__status__ = 'Development'

from password_validator import PasswordValidator

def default_validator():

    passwords = ("AAaa11!!")
    pv = PasswordValidator

    for p in passwords:
        if pv.is_valid(p):
            print(f'{pv} is a valid password')
        else:
            display_errors(pv)

        print()

if __name__ == '__main__':
    default_validator()

#!/user.bin.env python3

"""
This program is meant to pass a variety of password examples through a default and advanced password validator using
Object-Oriented Methods

default_validator runs the PasswordValidator class from password_validator. There the passwords are checked for if
they contain two capitol letters, lower case letters, numbers, and symbols.

advanced_validator runs the same previous conditions as well as a min-max length of 8 and 12 respectfully.

If the password passes a passing message is ran. If they do not pass, an exception is raised to tell the user why the
password doesn't work.

GitHub URL: https://github.com/RivarYoder01/PE2_Mod3_PasswordValidator
"""

__author__ = 'Rivar Yoder | Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/8/2024'
__status__ = 'Development'

from password_validator import PasswordValidator
from adv_pwd_validator import AdvPasswordValidator

DASH_LENGTH = 70


def display_errors(self):
    """
    Recei
    :param self:
    :return:
    """
    print(f'{self} is an invalid password')

    for e in self.get_errors():
        print(e)


def default_validator():
    """

    :return:
    """
    print('=' * DASH_LENGTH)
    print('Default Validator')
    print('Testing Passwords AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb')
    print('=' * DASH_LENGTH)
    print()

    passwords = ("AAaa11!!", "Abb12!!", "AAb12!", "AAbb1", "AAbb12!", "b!", "bb")
    pv = PasswordValidator()

    for p in passwords:
        if pv.is_valid(p):
            print(f'{pv} is a valid password')
        else:
            display_errors(pv)

        print()


def advanced_validator():
    """

    :return:
    """

    print('=' * DASH_LENGTH)
    print('Advanced Validator')  # Modify as needed while testing, delete this comment line before turn in -RY
    print('Testing Passwords AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb, AAbb!!12, AAbb!!12121212')
    print('=' * DASH_LENGTH)
    print()

    # Modify as needed while testing, delete this comment line before turn in -RY
    passwords = ("AAaa11!!", "Abb12!!", "AAb12!", "AAbb1", "AAbb12!", "b!", "bb", "AAbb!!12", "AAbb!!12121212")
    pv = AdvPasswordValidator()

    for p in passwords:
        if pv.is_valid(p):
            print(f'{pv} is a valid password')
        else:
            display_errors(pv)

        print()


if __name__ == '__main__':
    default_validator()
    advanced_validator()

    print('=' * DASH_LENGTH)
    print('Goodbye! :D')
    print('=' * DASH_LENGTH)




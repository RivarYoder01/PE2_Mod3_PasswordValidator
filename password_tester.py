#!/user.bin.env python3

"""
This program is meant to pass a variety of password examples through a default and advanced password validator using
Object-Oriented Methods

default_validator runs the PasswordValidator class from password_validator. There the passwords are checked for if
they contain two capitol letters, lower case letters, numbers, and symbols.

advanced_validator runs the same previous conditions as well as a min-max length of 8 and 12 respectfully.

If the password passes a passing message is run. If they do not pass, an exception is raised to tell the user why the
password doesn't work.

GitHub URL: https://github.com/RivarYoder01/PE2_Mod3_PasswordValidator
"""

__author__ = 'Rivar Yoder | Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/8/2024'
__status__ = 'Development'

from password_validator import PasswordValidator  # For use in default_validator
from adv_pwd_validator import AdvPasswordValidator  # For use in advanced_validator

DASH_LENGTH = 50


def display_errors(self):
    """
    Receives each successful password to display that a password failed the validator, runs a for loop to pull and
    display all errors found.

    :param self: An instance of the password validator
    :return: None
    """
    print(f'{self} is an invalid password')

    for e in self.get_errors():  # Pulls exact errors from password_validator and adv_pwd_validator
        print(e)


def default_validator():
    """
    Validates a set of passwords using the default password validator

    :return: None
    """
    print('=' * DASH_LENGTH)
    print('Default Validator')
    print('Testing The Following Passwords:')
    print('AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb')
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
    Runs an extended list of passwords to test the previous conditions as well as the new length and specific character
    conditions.

    :return: None
    """

    # Interface header to enhance readability
    print('=' * DASH_LENGTH)
    print('Advanced Validator')
    print('Testing The Following Passwords')
    print('AAaa11!!, Abb12!!, AAb12!, AAbb1, AAbb12!, b!, bb,')
    print('AAbb!(12, AAbb!!12121212')  # Added illegal symbol to test validate_specific_symbol
    print('=' * DASH_LENGTH)
    print()

    passwords = ("AAaa11!!", "Abb12!!", "AAb12!", "AAbb1", "AAbb12!", "b!", "bb", "AAbb!(12", "AAbb!!12121212")
    pv = AdvPasswordValidator()  # Runs the above password examples through the validator, pushing back as pv

    for p in passwords:  # Loops through each password to let the user know that password is valid
        if pv.is_valid(p):
            print(f'{pv} is a valid password')
        else:  # If a password is not valid
            display_errors(pv)

        print()  # Empty space between passwords


if __name__ == '__main__':
    default_validator()
    advanced_validator()

    print('=' * DASH_LENGTH)
    print('Goodbye! :D')
    print('=' * DASH_LENGTH)

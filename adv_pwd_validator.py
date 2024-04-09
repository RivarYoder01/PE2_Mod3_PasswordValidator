from password_exception import PasswordException
from password_validator import PasswordValidator


class AdvPasswordValidator(PasswordValidator):
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2,
                 char_min=8, char_max=12, symbol_min=2, valid_symbols=('@', '_', '!', '#', '$', '%', '&', '*', '?', '~')):
        """
        Defines the minimum and maximum character limit and which symbols can be used

        :param lowercase_min:
        :param uppercase_min:
        :param digit_min:
        :param char_min:
        :param char_max:
        :param symbol_min:
        :param valid_symbols:
        """

        super().__init__(lowercase_min, uppercase_min, digit_min, symbol_min)
        self._password = None
        self._errors = []  # Empty list that will store the errors found

        # assigns each parameter to objects that are attached to self
        self._char_min = char_min
        self._char_max = char_max
        self._valid_symbols = valid_symbols

    def get_errors(self):
        return self._errors

    def __str__(self):
        """
        Coverts password into a string

        :return:
        """
        return self._password

    def __validate_length(self):
        """
        char_count is used to track how many characters are in the string. If there are MORE than 8 characters then a
        custom minimum limit error is thrown. If there are LESS than 8 characters then a custom maximum limit error
        is thrown.

        :return:
        """

        char_count = len(self._password)

        if char_count < self._char_min:
            error = f"Contains {char_count} characters. Minimum is {self._char_min}"
            raise PasswordException(error, self._password)

        elif char_count > self._char_max:
            error = f"Contains {char_count} characters. Maximum is {self._char_max}"
            raise PasswordException(error, self._password)

    def __validate_specific_symbol(self):
        """
        Adds a list of specific symbols that will be allowed instead of any non-alphanumeric characters that the base
        symbol validator uses.
        :return: None
        """

        symbol_count = sum(1 for char in self._password if char in self._valid_symbols)

        if symbol_count < self._symbol_min:
            error = (f"Contains {symbol_count} symbol(s). Requires at least 2 symbols from the provided list: "
                     f"{self._valid_symbols}")
            raise PasswordException(error, self._password)

    def is_valid(self, password):
        """
        Runs each subclass above to check each parameter using a series of try excepts. If returned false, the error
        will be stored.

        :param password:
        :return:
        """

        # Should finally work!
        # Inherit and run validation rules from PasswordValidator
        super_result = super().is_valid(password)
        if not super_result:
            self._errors.extend(super().get_errors())

        try:  # Tests password for if it is between 8 and 12 characters
            self.__validate_length()
        except PasswordException as e:  # Stores error to be pulled by get_errors
            self._errors.append(e)

        try:
            self.__validate_specific_symbol()
        except PasswordException as e:
            self._errors.append(e)

        # Added this to delete duplicate error messages because for some reason the base validator error messages
        # would print twice
        self._errors = list(set(self._errors))

        if len(self._errors) == 0:
            return True
        else:
            return False

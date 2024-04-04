from password_exception import PasswordException


class PasswordValidator:
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2, symbol_min=2):
        """

        :param lowercase_min:
        :param uppercase_min:
        :param digit_min:
        :param symbol_min:
        """

        self._password = None
        self._lowercase_min = lowercase_min
        self._uppercase_min = uppercase_min
        self._digit_min = digit_min
        self._symbol_min = symbol_min

        self._errors = []

    def __validate_lowercase(self):
        """

        :return:
        """

        char_count = sum(1 for char in self._password if char.isalpha() and char.islower())

        if char_count < self._lowercase_min:
            error = f"Required {self._lowercase_min} lowercase letters but only contains {char_count}"
            raise PasswordException(error, self._password)
        # self.password == password

    def validate_upper_case(self):
        pass

    def is_valid(self, password):
        """

        :param password:
        :return:
        """

        self._password = password

        self._errors.clear()

        try:
            self.__validate_lowercase()
        except PasswordException as e:
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False

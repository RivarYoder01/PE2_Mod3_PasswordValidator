from password_exception import PasswordException


class AdvPasswordValidator:
    def __init__(self, char_min=8, char_max=12):
        """

        :param char_min:
        :param char_max:
        """

        self._password = None

        self._char_min = char_min
        self._char_max = char_max

        self._errors = []

    def __validate_length(self):
        """

        :return:
        """

        char_count = len(self._password)

        if char_count < self._char_min:
            error = f"Contains {char_count} characters. Minimum is {self._char_min}"
            raise PasswordException(error, self._password)

        elif char_count > self._char_max:
            error = f"Contains {char_count} characters. Maximum is {self._char_max}"
            raise PasswordException(error, self._password)

    def validate_specific_symbol(self, password):
        pass

    def get_errors(self):
        return self._errors

    def __str__(self):
        return self._password

    def is_valid(self, password):
        """

        :param password:
        :return:
        """

        self._password = password

        self._errors.clear()

        try:
            self.__validate_length()
        except PasswordException as e:
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False

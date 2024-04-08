from password_exception import PasswordException


class AdvPasswordValidator:
    def __init__(self, char_min=8, char_max=12):
        """
        Defines the minimum and maximum character limit and which symbols can be used

        :param char_min:
        :param char_max:
        """

        self._password = None
        self._errors = []  # Empty list that will store the errors found

        # assigns each parameter to objects that are attached to self
        self._char_min = char_min
        self._char_max = char_max

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

    def validate_specific_symbol(self, password):
        pass

    def is_valid(self, password):
        """
        Runs each subclass above to check each parameter using a series of try excepts. If returned false, the error
        will be stored.

        :param password:
        :return:
        """

        self._password = password  # Pulls in password to be checked
        self._errors.clear()  # Clears all stored errors

        try:  # Tests password for if it is between 8 and 12 characters
            self.__validate_length()
        except PasswordException as e:  # Stores error to be pulled by get_errors
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False

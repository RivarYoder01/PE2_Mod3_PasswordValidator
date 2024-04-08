from password_exception import PasswordException


class PasswordValidator:
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2, symbol_min=2):
        """
        Defines the parameters used to validate the passwords being passed through

        :param lowercase_min:
        :param uppercase_min:
        :param digit_min:
        :param symbol_min:
        """

        # assigns each parameter to objects that are attached to self
        self._password = None
        self._lowercase_min = lowercase_min
        self._uppercase_min = uppercase_min
        self._digit_min = digit_min
        self._symbol_min = symbol_min

        self._errors = []  # Empty list that will store the errors found

    def get_errors(self):
        return self._errors

    def __str__(self):
        return self._password

    def __validate_lowercase(self):
        """
        char_count is used to track how many letters are lowercase. A for loop checks each letter and adds 1 to
        char_count for every instance. If there are less than 2 lowercase letters then a custom error is thrown.

        :return:
        """

        # Adds 1 to each char in self._password if a character is alpha AND lowercase. Tracks the instances of this.
        char_count = sum(1 for char in self._password if char.isalpha() and char.islower())

        if char_count < self._lowercase_min:  # if there are less than 2 lowercase letters
            error = f"Required {self._lowercase_min} lowercase letters but only contains {char_count}"  # Error message
            raise PasswordException(error, self._password)  # Raises error exception

    def __validate_uppercase(self):
        """
        char_count is used to track how many letters are uppercase. A for loop checks each letter and adds 1 to
        char_count for every instance. If there are less than 2 uppercase letters then a custom error is thrown.

        :return:
        """

        # Adds 1 to each char in self._password if a character is alpha AND uppercase. Tracks the instances of this.
        char_count = sum(1 for char in self._password if char.isalpha() and char.isupper())

        if char_count < self._uppercase_min:  # if there are less than 2 uppercase letters
            error = f"Required {self._uppercase_min} uppercase letters but only contains {char_count}"  # Error message
            raise PasswordException(error, self._password)  # Raises error exception

    def __validate_digit(self):
        """

        :return:
        """

        char_count = sum(1 for char in self._password if char.isnumeric() and char.isnumeric())

        if char_count < self._digit_min:
            error = f"Required {self._digit_min} digits but only contains {char_count}"
            raise PasswordException(error, self._password)

    def __validate_symbols(self):
        """

        Asked ChatGPT to see how we can check for a symbol.
        https://chat.openai.com/share/14f25fec-41c0-4999-b1c4-7619f03f52a6
        :return:
        """

        char_count = sum(1 for char in self._password if not char.isalnum())

        if char_count < self._symbol_min:
            error = f"Required {self._symbol_min} symbols but only contains {char_count}"
            raise PasswordException(error, self._password)

    def is_valid(self, password):
        """

        :param password:
        :return:
        """

        self._password = password
        self._errors.clear()

        try:  # Tests password for if it contains at least two lower case letters
            self.__validate_lowercase()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_uppercase()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_digit()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_symbols()
        except PasswordException as e:
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False

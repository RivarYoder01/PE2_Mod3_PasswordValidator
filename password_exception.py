class PasswordException(Exception):
    def __init__(self, message, password):
        """

        :param message:
        :param password:
        """

        Exception.__init__(self)
        self.password = password

class PasswordException(Exception):
    def __init__(self, message, password):
        """

        :param message:
        :param password:
        """

        Exception.__init(self.message)
        self.password = password

class PasswordException(Exception):
    def __init__(self, message, password):
        """
        Initializes a new instance of PasswordException

        :param message: A descriptive error message indicating the reason for the exception
        :param password: The password associated with the validation error
        """

        Exception.__init__(self, message)
        self.password = password

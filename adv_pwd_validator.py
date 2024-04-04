from password_exception import PasswordException


class AdvPasswordValidator:
    def __init__(self):
        pass
        # properties

    def validate_lower_case(self, password):
        raise PasswordException("---")
        #self.password == password

    def validate_upper_case(self):
        pass

    def is_valid(self, password):
        #self.password == password
        self.validate_lower_case(password)
from password_exception import PasswordException

class PasswordValidator:
    def __init__(self):
        pass
        # properties

    def validate_lower_case(self, password):
        raise PasswordException("---")
        self.password == password

    def validate_upper_case(self):
        pass

    def is_valid(self, password):
        self.password == password

        try:
            self.validate_lower_case(password)
        except Exception as e:
            print(e)

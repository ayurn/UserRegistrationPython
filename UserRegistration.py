import re
import loggerfile
class UserRegistration :
    def __init__(self) :
        pass

    def first_name_regex(self, first_name):
        """
        Description:
            Function to validate first name.
        Parameter:
            first_name : get first name to validate
        """
        try:
            name_pattern = r"^[A-Z]{1}[a-zA-Z]{2,}$"
            return bool(re.match(name_pattern, first_name))
        except Exception :
            loggerfile.Logger("debug", "Invalid Program")

    def last_name_regex(self, last_name):
        """
           Description:
               Function to validate last name.
           Parameter:
               last_name : get last name to validate
           """
        try:
            name_pattern = r"^[A-Z]{1}[a-zA-Z]{2,}$"
            return bool(re.match(name_pattern, last_name))
        except Exception:
            loggerfile.Logger("debug", "Invalid Program")
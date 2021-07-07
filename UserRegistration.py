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

    def email_regex(self, email):
        """
       Description:
           Function to validate last name.
       Parameter:
           last_name : get last name to validate
       """
        try:
            email_pattern = "^[a-zA-Z0-9]{3,}([\\.\\+\\-]?[a-zA-Z0-9]{3,})?[@][A-Za-z0-9]{1,}[.][A-Za-z]{2,4}[,]?([.][A-Za-z]{2,4}[.]?)?$"
            return bool(re.match(email_pattern, email))
        except Exception:
            loggerfile.Logger("debug", "Invalid Program")

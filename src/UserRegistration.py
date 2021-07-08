
"""
@Author: Ayur Ninawe
@Date: 2021-07-07 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-08 15:15:30
@Title : user registration program with regex
"""

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
           Function to validate email.
       Parameter:
           email : get email to validate
       """
        try:
            email_pattern = "^[a-zA-Z0-9]{3,}([\\.\\+\\-]?[a-zA-Z0-9]{3,})?[@][A-Za-z0-9]{1,}[.][A-Za-z]{2,4}[,]?([.][A-Za-z]{2,4}[.]?)?$"
            return bool(re.match(email_pattern, email))
        except Exception:
            loggerfile.Logger("debug", "Invalid Program")

    def phone_number_regex(self, phone_number):
        """
       Description:
           Function to validate phone number.
       Parameter:
           phone_number : get phone_number to validate
       """
        try:
            phone_number_pattern = "^[9][1][ ][6-9][0-9]{9}$"
            return bool(re.match(phone_number_pattern, phone_number))
        except Exception:
            loggerfile.Logger("debug", "Invalid Program")


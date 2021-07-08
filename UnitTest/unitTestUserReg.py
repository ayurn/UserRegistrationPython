
"""
@Author: Ayur Ninawe
@Date: 2021-07-07 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-08 15:15:30
@Title : Testing code using Unit Test.
"""


import unittest
import sys
sys.path.insert(0, '/home/ayur/PycharmProjects/UserRegistration/src/')

from src.UserRegistration import UserRegistration

class TestUserRegistration(unittest.TestCase):

    def test_first_name_regex_givenCorrectName_shouldReturnTrue(self):
        """
        Description:
            Test case for checking Valid name.
        """
        first_name = "Ayur"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertTrue(result)

    def test_first_name_regex_giveIncorrectName_shouldReturnFalse(self):
        """
        Description:
            Test case for checking Invalid name.
        """
        first_name = "ayur"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertFalse(result)

    def test_last_name_regex_givenCorrectName_shouldReturnTrue(self):
        """
        Description:
            Test case for checking Valid last name.
        """
        last_name = "Ninawe"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertTrue(result)

    def test_last_name_regex_givenIncorrectName_shouldReturnFalse(self):
        """
        Description:
            Test case for checking Invalid last name.
        """
        last_name = "ninawe"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertFalse(result)

    def test_email_regex_givenCorrectEmail_shouldReturnTrue(self):
        """
        Description:
            Test case for checking Valid email.
        """
        email = "ninawe@gmail.com"
        user = UserRegistration()
        result = user.email_regex(email)
        self.assertTrue(result)

    def test_email_regex_givenIncorrectEmail_shouldReturnFalse(self):
        """
        Description:
            Test case for checking Invalid email.
        """
        email = "abc.100@hggdb.cvjhdb"
        user = UserRegistration()
        result = user.email_regex(email)
        self.assertFalse(result)

    def test_phone_number_regex_givenCorrectPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            Test case for checking Valid phone number.
        """
        phone_number = "91 8210029078"
        user = UserRegistration()
        result = user.phone_number_regex(phone_number)
        self.assertTrue(result)

    def test_phone_number_regex_givenIncorrectPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            Test case for checking invalid phone number.
        """
        phone_number = "918210029078"
        user = UserRegistration()
        result = user.phone_number_regex(phone_number)
        self.assertFalse(result)

    def test_password_regex_givenCorrectPassword_shouldReturnTrue(self):
        """
        Description:
            Test case for checking valid password
        """
        user = UserRegistration()
        self.assertTrue(user.password_regex("amcnfRwu@18"))
        self.assertTrue(user.password_regex("Ayur@nina123"))

    def test_password_regex_givenIncorrectPassword_shouldReturnFalse(self):
        """
        Description:
            Test case for checking invalid password
        """
        user = UserRegistration()
        self.assertFalse(user.password_regex("@nvgb"))
        self.assertFalse(user.password_regex("$rgrg"))
import unittest

from UserRegistration import UserRegistration

class TestUserRegistration(unittest.TestCase):

    def test_first_name_regex_givenCorrectName_shouldReturnTrue(self):
        first_name = "Ayur"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertTrue(result)

    def test_first_name_regex_giveIncorrectName_shouldReturnFalse(self):
        first_name = "ayur"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertFalse(result)
"""
@Author: Ayur Ninawe
@Date: 2021-07-07 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-08 19:15:30
@Title : Testing code using PyTest.
"""
import pytest
import sys
sys.path.insert(0, '/home/ayur/PycharmProjects/UserRegistration/src/')

from src.UserRegistration import UserRegistration
from src.emailTest import EmailTest

def test_first_name_should_return_true():
    """
    Description:
        Given valid name should return true and pass the test. 
    """
    first_name = "Ayur"
    user = UserRegistration()
    result = user.first_name_regex(first_name)
    assert(result)

def test_first_name_regex_giveIncorrectName_shouldReturnFalse():
    """
    Description:
        Test case for checking Invalid name.
    """
    with pytest.raises(Exception) as exc_info:
        first_name = "ayur"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        assert(result)

def test_last_name_regex_givenCorrectName_shouldReturnTrue():
    """
    Description:
        Test case for checking Valid last name.
    """
    last_name = "Ninawe"
    user = UserRegistration()
    result = user.last_name_regex(last_name)
    assert(result)

def test_last_name_regex_givenIncorrectName_shouldReturnFalse():
    """
    Description:
        Test case for checking Invalid last name.
    """
    with pytest.raises(Exception) as exc_info:
        last_name = "ninawe"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        assert(result)

def test_email_regex_givenCorrectEmail_shouldReturnTrue():
    """
    Description:
        Test case for checking Valid email.
    """
    email = "ninawe@gmail.com"
    user = UserRegistration()
    result = user.email_regex(email)
    assert(result)

def test_email_regex_givenIncorrectEmail_shouldReturnFalse():
    """
    Description:
        Test case for checking Invalid email.
    """
    with pytest.raises(Exception) as exc_info:
        email = "abc.100@hggdb.cvjhdb"
        user = UserRegistration()
        result = user.email_regex(email)
        assert(result)

def test_phone_number_regex_givenCorrectPhoneNumber_shouldReturnTrue():
    """
    Description:
        Test case for checking Valid phone number.
    """
    phone_number = "91 8210029078"
    user = UserRegistration()
    result = user.phone_number_regex(phone_number)
    assert(result)

def test_phone_number_regex_givenIncorrectPhoneNumber_shouldReturnTrue():
    """
    Description:
        Test case for checking invalid phone number.
    """
    with pytest.raises(Exception) as exc_info:
        phone_number = "918210029078"
        user = UserRegistration()
        result = user.phone_number_regex(phone_number)
        assert(result)

def test_password_regex_givenCorrectPassword_shouldReturnTrue():
    """
    Description:
        Test case for checking valid password
    """
    user = UserRegistration()
    assert(user.password_regex("avaArxyx@12"))
    assert(user.password_regex("123@xAyurwsar"))
    assert(user.password_regex("Ayur@ninawe123"))

def test_password_regex_givenIncorrectPassword_shouldReturnFalse():
    """
    Description:
        Test case for checking invalid password
    """
    with pytest.raises(Exception) as exc_info:
        user = UserRegistration()
        assert(user.password_regex("@nvgb"))
        assert(user.password_regex("$rgrg"))
        assert(user.password_regex("fdfer"))

def test_givenValidMultipleMails_shouldReturnTrue():
    """
    Description:
        this function validate multiple mails
    """
    user = UserRegistration()
    assert(user.multipleMailValidation(EmailTest.validMailIds))

def test_givenInvalidMultipleMails_shouldReturnFalse():
    """
    Description:
        this function validate multiple mails
    """
    with pytest.raises(Exception) as exc_info:
        user = UserRegistration()
        assert(user.multipleMailValidation(EmailTest.invalidMmailIds))
import pytest
import admin

AD = admin.admin()

def test_checkPassword_correctValue():
    """Checks password functionilty when password already entered is checked
    """
    name = AD.checkPassword("max")
    assert name == "max"

def test_checkPassword_incorrectValue():
    """Checks the checkpassword function when the password entered is one that is not entered
    """
    name = AD.checkPassword("jack")
    assert name == "Not found"

def test_checkPassword_incorrectParrameter():
    """Checks behaviour of checkpassword when a parameter that is not a string is given
    """
    name = AD.checkPassword(22)
    assert name == "Not found"


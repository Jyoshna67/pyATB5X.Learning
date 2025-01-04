import pytest
import allure
import requests
@allure.title("Verify that 2-2=0")
@allure.description("This is a basic math tc")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2==0
@allure.title("Verify that 2+2=4")
@allure.description("This is a basic math tc")
@pytest.mark.Regression
def test_basic_math1():
    assert 2+2==4
@allure.title("Verify that 3-3=0")
@allure.description("This is a basic math tc")
@pytest.mark.smoke
def test_basic_math2():
    assert 3-3==0
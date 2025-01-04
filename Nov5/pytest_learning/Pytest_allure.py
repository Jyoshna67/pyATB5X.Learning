import pytest
import allure

@allure.title("Verify that create booking,with valid data is working")
@allure.description("This testcase cakes for positive  create booking")

@pytest.mark.positive
def create_booking_positive():
    print("This is positive tc")
    assert 1-1==2
@allure.title("Verify that create booking,with invalid data is working")
@allure.description("This testcase cakes for negative create booking")

@pytest.mark.Negative
def create_booking_Negative_1():
    print("This is positive tc")
    assert 1 +1==2
@pytest.mark.Negative
def create_booking_Negative_2():
    print("This is positive tc")
    assert 1-1==0
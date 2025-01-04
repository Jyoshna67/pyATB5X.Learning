import pytest
import allure
import requests
@allure.title("Verify the Get request restful broker API")
@allure.description("This testcases checks booking id and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get= "https://restful-booker.herokuapp.com/booking"
    response_data=requests.get(url=url_get)
    print(response_data.text)
    assert(response_data.status_code==200)

@allure.title("Verify the Get request restful broker with invalid data")
@allure.description("This testcases checks booking -1 id and verify the response")
@pytest.mark.negative
def test_get_request_negative():
    url_get= "https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url=url_get)
    print(response_data.text)
    assert(response_data.status_code==404)




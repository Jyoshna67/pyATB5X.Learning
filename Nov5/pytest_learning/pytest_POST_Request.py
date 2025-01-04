import pytest
import allure
import requests


#To make a Request
@allure.title("TC1- Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud

def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"

    full_url= base_url+base_path_post
    headers={
        "Content-Type":"application/json"
    }
    payload={
        {
            "firstname": "Jim",
            "lastname": "Brown",
            "total price": 111,
            "deposit paid": True,
            "booking dates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additional needs": "Breakfast"
        }
    }
    response_data = requests.post(url=full_url,headers=headers,json=payload)

    #To check status code 
    assert response_data.status_code==200
#Booking ID>0,firstname==Jim

  response_data_json = response_data.json()
  bookingid=response_data_json["bookingid"]






# API Request- GET
import pytest
import requests
import requests.cookies


def test_get_single_request_by_ID():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response.json())
    response_status = response.status_code
    assert response_status == 200
    
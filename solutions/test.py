# SOLUTION EXERCISE 8
import requests
import pytest
import json

BASE_URL = "https://simple-books-api.glitch.me"

# TEST API STATUS
def test_api_request():
    url = f"{BASE_URL}/status"
    response = requests.get(url)

    # Check the response status code
    assert response.status_code == 200
    data = response.json()

    # Check if the expected key is in the response data
    assert "status" in data
    assert data["status"] == "OK"

    print("API response data:")
    print(data)


# TEST BOOK DETAILS
@pytest.mark.parametrize("book_id", [1, 2, 3, 4, 5, 6])
def test_get_book_details(book_id):

    url = f"{BASE_URL}/books/{book_id}"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "type" in data
    assert "available" in data

    print("API response data:")
    print(data)


# TEST INVALID BOOK ID
@pytest.mark.parametrize("invalid_book_id", ["abc", "!@#$", 0, -1])
def test_invalid_book_id(invalid_book_id):

    url = f"{BASE_URL}/books/{invalid_book_id}"
    response = requests.get(url)

    assert response.status_code == 404


# TEST FOR SUBMITTING ORDER
token = "f1b925a26f9c833469ec05c2b861f4e2c2280fa960dc399c9a9f0e2dbf6822d5"
def test_submit_order():
    url = f"{BASE_URL}/orders"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    order_data = {
      "bookId": 5,
      "customerName": "Luigi"
    }
    response = requests.post(url, data=json.dumps(order_data), headers=headers)
    assert response.status_code == 201, f"Expected status code 200, but got {response.status_code}"

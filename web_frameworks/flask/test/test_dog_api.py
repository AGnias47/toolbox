import pytest
import requests

"""
This is done now by manually running the flask server
"""

BASE_URL = "http://localhost:5000"


def test_dog_endpoint():
    requests.post(
        BASE_URL + "/dog",
        json={"name": "Peggy", "type": "Pit Mix", "weight": 42, "playfulness": 7},
    )
    find_peggy = False
    for dog_id, dog_data in requests.get(BASE_URL + "/dog").json().items():
        if dog_data["name"] == "Peggy":
            find_peggy = True
            break
    assert find_peggy
    requests.get(BASE_URL + "/dog")


def test_dog_id_endpoint():
    dog_data = requests.get(BASE_URL + "/dog").json()
    dog_id = list(dog_data.keys())[0]
    assert dog_data[dog_id] == requests.get(BASE_URL + f"/dog/{dog_id}").json()
    requests.delete(BASE_URL + f"/dog/{dog_id}")
    assert dog_id not in requests.get(BASE_URL + "/dog").json()


if __name__ == "__main__":
    pytest.main()

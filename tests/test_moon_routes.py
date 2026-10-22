
def test_create_moon_with_planet(client, one_planet):
    test_data = {
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }

    response = client.post("/planets/1/moons", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }


def test_create_moon_with_nonexistent_planet(client):
    test_data = {
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }

    response = client.post("/planets/1/moons", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}


def test_get_moons_by_planet(client, one_planet):
    response = client.post("/planets/1/moons", json={
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    })

    assert response.status_code == 201

    response = client.get("/planets/1/moons")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }]


def test_get_moons_by_planet_with_no_moons(client, one_planet):
    response = client.get("/planets/1/moons")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

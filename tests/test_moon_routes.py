def test_create_one_moon(client):
    # Act
    response = client.post("/moons", json={
        "name": "New Moon",
        "size": 2000,
        "description": "A good thing"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Moon",
        "size": 2000,
        "description": "A good thing"
    }

def test_create_one_moon_no_name(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/moons", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}

def test_get_all_moons_one_saved_moon(client, one_saved_moon):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "New Moon",
    }

def test_get_all_moons_no_saved_moon(client):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []    

def test_create_moon_with_planet(client, one_saved_moon):
    # Arrange
    test_data = {
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }

    # Act
    response = client.post("/moons/1/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Moon",
        "size": 2000,
        "description": "The Best!"
    }

def test_create_moon_with_nonexistant_planet(client):
    # Arrange
    test_data = {
        "name": "New moon",
        "description": "The Best!"
    }

    # Act
    response = client.post("/planets/1/moons", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Moon 1 not found"}

def test_create_planet_with_bad_moon_id(client):
    # Arrange
    test_data = {
        "name": "New Planet",
        "description": "The Best!"
    }

    # Act
    response = client.post("/moons/cat/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Moon cat invalid"}

def test_get_planets_by_moon_expects_two_planets(client, a_saved_planets, moon_with_two_planets):
    # Act
    response = client.get("/moons/1/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {
            "id": 3,
            "name": "Desert Planet",
            "description": "Sands all around",
            "moon_id": 1
        },
        {
            "id": 4,
            "name": "Plains Planet",
            "description": "Grasslands for miles",
            "moon_id": 1
        }
    ]

def test_get_planets_by_moon_with_no_planets(client, one_saved_moon):
    # Act
    response = client.get("/moons/1/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []
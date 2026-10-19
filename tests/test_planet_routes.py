def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

# Test 1: GET /planets/1 no existis
def test_get_one_planet_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

#Test 2 GET /planets/1 
def test_get_one_planet_returns_planet(client, one_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["distance"] == one_planet.distance

# Test 3: GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_all_planet_returns_planets(client, all_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0]["id"] == all_saved_planets[0].id
    assert response_body[1]["name"] == all_saved_planets[1].name
    assert response_body[0]["description"] == all_saved_planets[0].description
    assert response_body[1]["distance"] == all_saved_planets[1].distance

#Test 4: POST /planets with a JSON request body returns a 201
def test_create_one_planet(client):
    new_planet = {
        "id": 3,
        "name": "Rayne",
        "description": "The Best planet in the space!",
        "distance": 3
    }
    response = client.post("/planets", json=new_planet)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["name"] == "Rayne"
from app.routes.route_utilities import validate_model
from app.models.planet import Planet
from werkzeug.exceptions import HTTPException
import pytest

def test_validate_model(all_saved_planets):
    # Act
    result_planet = validate_model(Planet, 1)

    # Assert
    assert result_planet.id == 1
    assert result_planet.name == "Earth"
    assert result_planet.description == "Our home planet"

def test_validate_model_missing_record(all_saved_planets):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_planet = validate_model(Planet, "3")

    response = error.value.response
    assert response.status == "404 NOT FOUND"
    
def test_validate_model_invalid_id(all_saved_planets):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_planet = validate_model(Planet, "cat")

    response = error.value.response
    assert response.status == "400 BAD REQUEST"
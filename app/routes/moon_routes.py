from flask import Blueprint, request
from app.models.moon import Moon
from app.models.planet import Planet
from .route_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint("moons_bp", __name__, url_prefix="/planets")

@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)


@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    response = [moon.to_dict() for moon in planet.moons]
    return response



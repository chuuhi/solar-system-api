import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.planet import Planet
from dotenv import load_dotenv
import os


load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet = Planet(id=1,
                    name="Mars",
                    description="Good planet beside us",
                    distance=20000)

    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def all_saved_planets(app):
    # Arrange
    planet1 = Planet(id=1,
                    name="Earth",
                    description="Our home planet",
                    distance=20000)
    planet2 = Planet(id=2,
                    name="Mercury",
                    description="Cool planet far from us",
                    distance=1000000)

    db.session.add_all([planet1, planet2])
    db.session.commit()
    return [planet1, planet2]
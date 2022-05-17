from app import app as create_app
import pytest


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_json_data(client):
    response = client.get("/")
    print(response.json)
    assert response.json["hello"] == "Welcome to the world of tommorow!"

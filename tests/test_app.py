import pytest
from flask_test_and_coverage.app import app

@pytest.fixture
def client():
    """
    Fixture to create a test client for our Flask application.
    """
    # configures our Flask app for testing
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """
    Test that the root endpoint returns 'Hello World!'
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World!" in response.data

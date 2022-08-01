from run import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_if_home_return_status_200():
    response = client.get('/')

    assert response.json() == {"msg": 'Welcome to api'}
    assert response.status_code == 200

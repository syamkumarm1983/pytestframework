import pytest
from utils1.myapiclient import MyAPIClient

@pytest.fixture(scope="class")
def user_api(config, session):
    session.headers.update({'thisis': 'users',"x-api-key":"reqres-free-v1"})
    myseesion = MyAPIClient(config['user_service'],session)
    return myseesion

@pytest.mark.user_api
def test_get_users(user_api):
    res = user_api.get("/users?page=2")
    assert res.status_code == 200
    data = res.json()
    assert "data" in data

@pytest.mark.users
def test_create_user(user_api):
    payload = {"name": "Syam", "job": "QA Engineer"}
    res = user_api.post("/users", data=payload)
    assert res.status_code == 201
    assert res.json()["name"] == "Syam"

@pytest.mark.users
@pytest.mark.parametrize('id',[(2)])
def test_getUser(user_api,id):
        res = user_api.get(f"/api/users/{id}")
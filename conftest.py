import pytest
import json
import requests
from utils1.myrequestFilter import MyrequestFilter

def pytest_addoption(parser):
    parser.addoption( "--env", action="store", default="qa", help="Environment: qa or staging")

@pytest.fixture(scope='session')
def config(pytestconfig):
    with open('config.json') as f:
        data =json.load(f)
    env = pytestconfig.getoption("env")
    return data['environment'][env]


@pytest.fixture(scope="session",autouse=True)
def session():
    s = MyrequestFilter()
    s.headers.update({"Content-Type": "application/json"})
    # s.headers.update({"Content-Type": "application/json syam"})
    return s
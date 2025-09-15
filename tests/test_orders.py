import pytest
from utils1.myapiclient import MyAPIClient

@pytest.fixture(scope='class')
def moduleScofe(config,session):
    session.headers.update({'thisis': 'orders'})
    myseesion = MyAPIClient(config['order_service'],session)
    return myseesion

@pytest.mark.moduleScofe
def test_get_products(moduleScofe):
    res = moduleScofe.get("/products")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
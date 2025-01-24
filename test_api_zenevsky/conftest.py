import pytest

from test_api_zenevsky.endpoints.create_object import CreateObject
from test_api_zenevsky.endpoints.update_object import UpdateObject
from test_api_zenevsky.endpoints.patch_object import PatchObject
from test_api_zenevsky.endpoints.get_object import GetObject
from test_api_zenevsky.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope='function')
def create_and_delete_object(create_object_endpoint, delete_object_endpoint):
    payload = {"name": "test", "data": {"field_1": "value_1", "field_2": True}}
    create_object_endpoint.create_object(payload)
    object_id = create_object_endpoint.object_id
    yield object_id
    delete_object_endpoint.delete_object(object_id)


@pytest.fixture(scope='function')
def create_object_precondition(create_object_endpoint):
    payload = {"name": "test", "data": {"field_1": "value_1", "field_2": True}}
    create_object_endpoint.create_object(payload)
    return create_object_endpoint.object_id

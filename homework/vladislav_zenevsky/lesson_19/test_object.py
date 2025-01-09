import requests
import pytest


@pytest.fixture(scope='function')
def create_and_delete_object():
    body = {"name": "test", "data": {"field_1": "value_1", "field_2": True}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope='function')
def create_object():
    body = {"name": "test", "data": {"field_1": "value_1", "field_2": True}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    return object_id


@pytest.fixture(scope='session')
def session_status():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def really_useful_fixture():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
@pytest.mark.parametrize(
    'body',
    [
        {"name": "test", "data": {"field_1": "value_1"}},
        {"name": "test", "data": {"field_1": "value_1", "field_2": True}},
        {"name": "test", "data": {"field_1": [{"field_1": "value_1"}, {"field_1": "value_1"}]}}
    ]
)
def test_create_object_with_valid_body(body, session_status, really_useful_fixture):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    object_id = response.json()['id']
    requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')


@pytest.mark.medium
@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Create object name missing', {"data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data missing', {"name": "test"}),
        ('Create object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data wrong type', {"name": "True", "data": 7})
    ]
)
def test_create_object_with_invalid_body(test_name, body, session_status, really_useful_fixture):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'[{test_name}] Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'body',
    [
        {"name": "test", "data": {"field_1": "value_1"}},
        {"name": "test", "data": {"field_1": "value_1", "field_2": True}},
        {"name": "test", "data": {"field_1": [{"field_1": "value_1"}, {"field_1": "value_1"}]}}
    ]
)
def test_update_object_with_valid_body(body, session_status, really_useful_fixture, create_and_delete_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Create object name missing', {"data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data missing', {"name": "test"}),
        ('Create object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data wrong type', {"name": "True", "data": 7})
    ]
)
def test_update_object_with_invalid_body(test_name, body, session_status, really_useful_fixture,
                                         create_and_delete_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'[{test_name}] Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Patch object all fields are filled', {"name": "test", "data": {"field_1": "value_1"}}),
        ('Patch object name missing', {"data": {"field_1": "value_1", "field_2": True}}),
        ('Patch object data missing', {"name": "test"}),
    ]
)
def test_patch_object_with_valid_body(test_name, body, session_status, really_useful_fixture, create_and_delete_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Patch object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Patch object data wrong type', {"name": "True", "data": 7})
    ]
)
def test_patch_object_with_invalid_body(test_name, body, session_status, really_useful_fixture,
                                        create_and_delete_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'[{test_name}] Incorrect response status code: {response.status_code}'


def test_delete_object_existing(session_status, really_useful_fixture, create_object):
    response = requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    assert response.status_code == 200


def test_delete_object_not_existing(session_status, really_useful_fixture, create_object):
    requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    response = requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    assert response.status_code == 404


def test_get_object_existing(session_status, really_useful_fixture, create_and_delete_object):
    response = requests.get(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    assert response.status_code == 200


def test_get_object_not_existing(session_status, really_useful_fixture, create_and_delete_object):
    requests.delete(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    response = requests.get(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    assert response.status_code == 404

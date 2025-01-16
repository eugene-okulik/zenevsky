import requests
import pytest
import allure


@pytest.fixture(scope='function')
def create_and_delete_object():
    with allure.step('Run "Create object" request to create a new object'):
        body = {"name": "test", "data": {"field_1": "value_1", "field_2": True}}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            url='http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
        object_id = response.json()['id']
    yield object_id
    with allure.step('Run "Delete object" request to delete the object'):
        requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope='function')
def create_object():
    with allure.step('Run "Create object" request to create a new object'):
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


@pytest.mark.parametrize(
    'body',
    [
        {"name": "test", "data": {"field_1": "value_1"}},
        {"name": "test", "data": {"field_1": "value_1", "field_2": True}},
        {"name": "test", "data": {"field_1": [{"field_1": "value_1"}, {"field_1": "value_1"}]}}
    ]
)
@pytest.mark.critical
@allure.feature('Objects')
@allure.story('Create object')
@allure.title('Create object with correct body')
def test_create_object_with_valid_body(body, session_status, really_useful_fixture):
    with allure.step('Run "Create object" request with correct body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            url='http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    object_id = response.json()['id']
    requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Create object name missing', {"data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data missing', {"name": "test"}),
        ('Create object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Create object data wrong type', {"name": "True", "data": 7})
    ]
)
@pytest.mark.medium
@allure.feature('Objects')
@allure.story('Create object')
@allure.title('Create object with invalid body')
def test_create_object_with_invalid_body(test_name, body, session_status, really_useful_fixture):
    with allure.step('Run "Create object" request with invalid body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            url='http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 400'):
        assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'body',
    [
        {"name": "test", "data": {"field_1": "value_1"}},
        {"name": "test", "data": {"field_1": "value_1", "field_2": True}},
        {"name": "test", "data": {"field_1": [{"field_1": "value_1"}, {"field_1": "value_1"}]}}
    ]
)
@allure.feature('Objects')
@allure.story('Update object')
@allure.title('Update object with correct body')
def test_update_object_with_valid_body(body, session_status, really_useful_fixture, create_and_delete_object):
    with allure.step('Run "Update object" request with correct body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
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
@allure.feature('Objects')
@allure.story('Update object')
@allure.title('Update object with invalid body')
def test_update_object_with_invalid_body(test_name, body, session_status, really_useful_fixture,
                                         create_and_delete_object):
    with allure.step('Run "Update object" request with invalid body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 400'):
        assert response.status_code == 400, f'[{test_name}] Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Patch object all fields are filled', {"name": "test", "data": {"field_1": "value_1"}}),
        ('Patch object name missing', {"data": {"field_1": "value_1", "field_2": True}}),
        ('Patch object data missing', {"name": "test"}),
    ]
)
@allure.feature('Objects')
@allure.story('Patch object')
@allure.title('Patch object with correct body')
def test_patch_object_with_valid_body(test_name, body, session_status, really_useful_fixture, create_and_delete_object):
    with allure.step('Run "Patch object" request with correct body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Patch object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Patch object data wrong type', {"name": "True", "data": 7})
    ]
)
@allure.feature('Objects')
@allure.story('Patch object')
@allure.title('Patch object with invalid body')
def test_patch_object_with_invalid_body(test_name, body, session_status, really_useful_fixture,
                                        create_and_delete_object):
    with allure.step('Run "Patch object" request with invalid body'):
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(
            url=f'http://167.172.172.115:52353/object/{create_and_delete_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 400'):
        assert response.status_code == 400, f'[{test_name}] Incorrect response status code: {response.status_code}'


@allure.feature('Objects')
@allure.story('Delete object')
@allure.title('Delete existing object')
def test_delete_object_existing(session_status, really_useful_fixture, create_object):
    with allure.step('Run "Delete object" request for created object'):
        response = requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200


@allure.feature('Objects')
@allure.story('Delete object')
@allure.title('Delete not-existing object')
def test_delete_object_not_existing(session_status, really_useful_fixture, create_object):
    with allure.step('Run "Delete object" request for created object'):
        requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    with allure.step('Run "Delete object" request for already deleted object'):
        response = requests.delete(url=f'http://167.172.172.115:52353/object/{create_object}')
    with allure.step('Check status code is 404'):
        assert response.status_code == 404


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get existing object')
def test_get_object_existing(session_status, really_useful_fixture, create_and_delete_object):
    with allure.step('Run "Get object" request for created object'):
        response = requests.get(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get not-existing object')
def test_get_object_not_existing(session_status, really_useful_fixture, create_and_delete_object):
    with allure.step('Run "Delete object" request for created object'):
        requests.delete(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    with allure.step('Run "Get object" request for already deleted object'):
        response = requests.get(url=f'http://167.172.172.115:52353/object/{create_and_delete_object}')
    with allure.step('Check status code is 404'):
        assert response.status_code == 404

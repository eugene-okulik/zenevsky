import requests


def pre_condition_create_object():
    body = {
        "name": "test",
        "data": {
            "field_1": "value_1",
            "field_2": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def post_condition_delete_object(object_id):
    requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')


def create_object_all_fields_are_filled():
    body = {
        "name": "test",
        "data": {
            "field_1": "value_1",
            "field_2": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(response.json()['id'])


def create_object_name_missing():
    body = {
        "data": {
            "field_1": "value_1",
            "field_2": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'


def create_object_data_missing():
    body = {
        "name": "test"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'


def create_object_name_wrong_type():
    body = {
        "name": True,
        "data": {
            "field_1": "value_1",
            "field_2": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'


def create_object_data_wrong_type():
    body = {
        "name": "True",
        "data": 7
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url='http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'


def update_object_all_fields_are_filled():
    object_id = pre_condition_create_object()
    body = {
        "name": "test_upd",
        "data": {
            "field_1": "value_1_upd",
            "field_2": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    assert response.json()['name'] == body['name'] and response.json()['data'] == body['data']
    post_condition_delete_object(object_id)


def update_object_name_missing():
    object_id = pre_condition_create_object()
    body = {
        "data": {
            "field_1": "value_1_upd",
            "field_2": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def update_object_data_missing():
    object_id = pre_condition_create_object()
    body = {
        "name": "test_upd"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def update_object_wrong_name_type():
    object_id = pre_condition_create_object()
    body = {
        "name": 7,
        "data": {
            "field_1": "value_1_upd",
            "field_2": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def update_object_wrong_data_type():
    object_id = pre_condition_create_object()
    body = {
        "name": "test_upd",
        "data": False
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def patch_object_all_fields_are_filled():
    object_id = pre_condition_create_object()
    body = {
        "name": "test_patched",
        "data": {
            "field_1": "value_1_patched",
            "field_2": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    assert response.json()['name'] == body['name'] and response.json()['data'] == body['data']
    post_condition_delete_object(object_id)


def patch_object_name_missing():
    object_id = pre_condition_create_object()
    body = {
        "data": {
            "field_1": "value_1_patched",
            "field_2": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    assert response.json()['data'] == body['data']
    post_condition_delete_object(object_id)


def patch_object_data_missing():
    object_id = pre_condition_create_object()
    body = {
        "name": "test_patched"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f'Incorrect response status code: {response.status_code}'
    assert response.json()['name'] == body['name']
    post_condition_delete_object(object_id)


def patch_object_name_wrong_type():
    object_id = pre_condition_create_object()
    body = {
        "name": {
            "test_patched": 4
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def patch_object_data_wrong_type():
    object_id = pre_condition_create_object()
    body = {
        "data": [
            {
                "test_patched": 4
            }
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        url=f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, f'Incorrect response status code: {response.status_code}'
    post_condition_delete_object(object_id)


def delete_object_existing():
    object_id = pre_condition_create_object()
    response = requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200


def delete_object_not_existing():
    object_id = pre_condition_create_object()
    requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')
    response = requests.delete(url=f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 404


create_object_all_fields_are_filled()
create_object_name_missing()
create_object_data_missing()
create_object_name_wrong_type()
create_object_data_wrong_type()
update_object_all_fields_are_filled()
update_object_name_missing()
update_object_data_missing()
update_object_wrong_name_type()
update_object_wrong_data_type()
patch_object_all_fields_are_filled()
patch_object_name_missing()
patch_object_data_missing()
patch_object_name_wrong_type()
patch_object_data_wrong_type()
delete_object_existing()
delete_object_not_existing()

import pytest
import allure


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
def test_create_object_with_valid_body(create_object_endpoint, delete_object_endpoint, body):
    create_object_endpoint.create_object(body)
    create_object_endpoint.check_that_status_is_200()
    object_id = create_object_endpoint.object_id
    delete_object_endpoint.delete_object(object_id)


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
def test_create_object_with_invalid_body(create_object_endpoint, test_name, body):
    create_object_endpoint.create_object(body)
    create_object_endpoint.check_that_status_is_400()


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
def test_update_object_with_valid_body(body, create_and_delete_object, update_object_endpoint):
    update_object_endpoint.update_object(body, create_and_delete_object)
    update_object_endpoint.check_that_status_is_200()


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
def test_update_object_with_invalid_body(test_name, body, create_and_delete_object, update_object_endpoint):
    update_object_endpoint.update_object(body, create_and_delete_object)
    update_object_endpoint.check_that_status_is_400()


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
def test_patch_object_with_valid_body(test_name, body, create_and_delete_object, patch_object_endpoint):
    patch_object_endpoint.patch_object(body, create_and_delete_object)
    patch_object_endpoint.check_that_status_is_200()


@pytest.mark.parametrize(
    'test_name, body',
    [
        ('Patch object name wrong type', {"name": True, "data": {"field_1": "value_1", "field_2": True}}),
        ('Patch object data wrong type', {"name": "True", "data": 7})
    ]
)
@allure.feature('Objects')
@allure.story('Patch object')
@allure.title('Patch object with incorrect body')
def test_patch_object_with_invalid_body(test_name, body, create_and_delete_object, patch_object_endpoint):
    patch_object_endpoint.patch_object(body, create_and_delete_object)
    patch_object_endpoint.check_that_status_is_400()


@allure.feature('Objects')
@allure.story('Delete object')
@allure.title('Delete existing object')
def test_delete_object_existing(create_object_precondition, delete_object_endpoint):
    delete_object_endpoint.delete_object(create_object_precondition)
    delete_object_endpoint.check_that_status_is_200()


@allure.feature('Objects')
@allure.story('Delete object')
@allure.title('Delete not-existing object')
def test_delete_object_not_existing(create_object_precondition, delete_object_endpoint):
    delete_object_endpoint.delete_object(create_object_precondition)
    delete_object_endpoint.delete_object(create_object_precondition)
    delete_object_endpoint.check_that_status_is_404()


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get existing object')
def test_get_object_existing(create_and_delete_object, get_object_endpoint):
    get_object_endpoint.get_object(create_and_delete_object)
    get_object_endpoint.check_that_status_is_200()


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get not-existing object')
def test_get_object_not_existing(create_and_delete_object, delete_object_endpoint, get_object_endpoint):
    delete_object_endpoint.delete_object(create_and_delete_object)
    get_object_endpoint.get_object(create_and_delete_object)
    get_object_endpoint.check_that_status_is_404()

from api.gorestapi.go_rest_api import GoRestApi
import pytest


@pytest.fixture()
def init_objects():
    go_rest_api = GoRestApi()
    yield go_rest_api


# get male and female gender count and make them even via api requests
def test_gender_equality(init_objects):
    go_rest_api = init_objects
    responses = go_rest_api.create_even_genders()
    assert all(response.status_code == 201 for response in responses)
    male_count = go_rest_api.get_male_count()
    female_count = go_rest_api.get_female_count()
    assert male_count == female_count


# get all inactive users and delete them all
def test_delete_inactive_users(init_objects):
    go_rest_api = init_objects
    responses = go_rest_api.delete_inactive_users()
    assert all(response.status_code == 204 for response in responses)
    inactive_users = go_rest_api.get_inactive_users()
    assert inactive_users == []


def test_replace_email_extensions_with_co_il(init_objects):
    go_rest_api = init_objects
    responses = go_rest_api.replace_email_extension()
    assert all(response.status_code == 204 for response in responses)
    users_email_extensions = go_rest_api.get_users_email_extensions()
    assert all(extension == "co.il" for extension in users_email_extensions)

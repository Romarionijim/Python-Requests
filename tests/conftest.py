from api.gorestapi.go_rest_api import GoRestApi
import pytest


@pytest.fixture()
def init_objects():
    go_rest_api = GoRestApi()
    yield go_rest_api

import pytest
import requests
from endpoints.get_object import GetObject
from endpoints.post_object import PostObject
from endpoints.update_object import PutObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def post_object_endpoint():
    return PostObject()


@pytest.fixture()
def put_object_endpoint():
    return PutObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_post_id(post_object_endpoint, delete_object_endpoint, get_object_endpoint):
    payload = {"name": "My object",
            "data": {"color": "red",
                     "size": "medium"}}
    post_id = post_object_endpoint.post_object(payload=payload).json()['id']
    yield post_id
    delete_object_endpoint.delete_object(post_id)

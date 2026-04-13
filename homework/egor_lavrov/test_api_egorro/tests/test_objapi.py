import pytest
import requests
from endpoints.endpoint import Endpoint


TEST_DATA = [
    {"name": "Apple_1", "data": {"color": "red", "size": "small"}},
    {"name": "Apple_2", "data": {"color": "yellow", "size": "medium"}},
    {"name": "Apple_3", "data": {"color": "green", "size": "big"}}
]


def test_api_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_object()
    get_object_endpoint.assert_status_code_is(200)


def test_api_get_the_object(get_object_endpoint, new_post_id):
    get_object_endpoint.get_object(object_id=new_post_id)
    get_object_endpoint.assert_status_code_is(200)


@pytest.mark.parametrize('payload', TEST_DATA)
def test_api_create_new_object(post_object_endpoint, payload):
    post_object_endpoint.post_object(payload=payload)
    post_object_endpoint.assert_status_code_is(200)
    post_object_endpoint.assert_name_in_response_matches_payload(payload['name'])
    post_object_endpoint.assert_color_in_response_matches_payload(payload['data']['color'])
    post_object_endpoint.assert_size_in_response_matches_payload(payload['data']['size'])


@pytest.mark.parametrize('payload', TEST_DATA)
def test_api_update_object(put_object_endpoint, new_post_id, payload):
    put_object_endpoint.put_object(object_id=new_post_id, payload=payload)
    put_object_endpoint.assert_status_code_is(200)
    put_object_endpoint.assert_name_in_response_matches_payload(payload['name'])
    put_object_endpoint.assert_color_in_response_matches_payload(payload['data']['color'])
    put_object_endpoint.assert_size_in_response_matches_payload(payload['data']['size'])


def test_api_patch_object(patch_object_endpoint, new_post_id):
    payload = {"name": "My updated object",
            "data": {"color": "yellow"}
               }
    patch_object_endpoint.patch_object(object_id=new_post_id, payload=payload)
    patch_object_endpoint.assert_status_code_is(200)
    patch_object_endpoint.assert_name_in_response_matches_payload(payload['name'])
    patch_object_endpoint.assert_color_in_response_matches_payload(payload['data']['color'])


def test_api_delete_object(delete_object_endpoint, new_post_id):
    delete_object_endpoint.delete_object(object_id=new_post_id)
    delete_object_endpoint.assert_status_code_is(200)
    
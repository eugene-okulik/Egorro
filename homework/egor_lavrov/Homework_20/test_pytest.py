import requests
import pytest


@pytest.fixture(autouse=True, scope='session')
def start_complete_text():
    print('\nStart testing')
    yield
    print('\nTesting complete')


@pytest.fixture(autouse=True)
def after_before_text():
    print('\nBefore testing')
    yield
    print('\nAfter testing')


@pytest.fixture()
def new_post_id():
    body = {"name": "My object",
            "data": {"color": "red",
                     "size": "medium"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


def test_get_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200


def test_get_the_object(new_post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == new_post_id, 'Wrong id'


@pytest.mark.critical
@pytest.mark.parametrize('body', [{"name": "Apple_1", "data": {"color": "red", "size": "small"}},
                                  {"name": "Apple_2", "data": {"color": "yellow", "size": "medium"}},
                                  {"name": "Apple_3", "data": {"color": "green", "size": "big"}}])
def test_add_post(body):
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == response.json()['id'], 'Wrong id'
    assert response.json()['name'] == body['name'], 'Wrong name'
    assert response.json()['data']['color'] == body['data']['color'], 'Wrong color'
    assert response.json()['data']['size'] == body['data']['size'], 'Wrong size'


def test_put_the_post(new_post_id):
    body = {"name": "My updated object",
            "data": {"color": "blue",
                     "size": "small"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == str(new_post_id), 'Wrong id'
    assert response.json()['name'] == 'My updated object', 'Wrong name'
    assert response.json()['data']['color'] == 'blue', 'Wrong color'
    assert response.json()['data']['size'] == 'small', 'Wrong size'


def test_patch_the_post(new_post_id):
    body = {"name": "My updated object",
            "data": {"color": "yellow",
                     "size": "small"}}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == new_post_id, 'Wrong id'
    assert response.json()['data']['color'] == 'yellow', 'Wrong color'


@pytest.mark.medium
def test_delete_a_post(new_post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    assert response.status_code == 200, 'Wrong status code'

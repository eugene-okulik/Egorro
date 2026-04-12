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

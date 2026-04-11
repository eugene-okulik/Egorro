import requests


def new_post():
    body = {"name": "My object",
            "data": {"color": "red",
                     "size": "medium"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers)
    return response.json()['id']


def clear(post_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


def get_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200


def get_object(id):
    post_id = id
    response = requests.get('http://objapi.course.qa-practice.com/object/1')
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == post_id, 'Wrong id'


def add_post():
    body = {"name": "My object",
            "data": {"color": "red",
                     "size": "medium"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers)
    assert response.status_code == 200, 'Wrong status code'


def put_the_post():
    post_id = new_post()
    body = {"name": "My updated object",
            "data": {"color": "blue",
                     "size": "small"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{post_id}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == str(post_id), 'Wrong id'
    assert response.json()['name'] == 'My updated object', 'Wrong name'
    assert response.json()['data']['color'] == 'blue', 'Wrong color'
    assert response.json()['data']['size'] == 'small', 'Wrong size'
    clear(post_id)


def patch_the_post():
    post_id = new_post()
    body = {"name": "My updated object",
            "data": {"color": "yellow",
                     "size": "small"}}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{post_id}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['id'] == post_id, 'Wrong id'
    assert response.json()['data']['color'] == 'yellow', 'Wrong color'
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code == 200, 'Wrong status code'


get_objects()
get_object(1)
put_the_post()
patch_the_post()
delete_a_post()

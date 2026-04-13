import requests
import pytest
import allure


@allure.title('Получение всех объектов')
@allure.feature('Метод GET')
@allure.story('Получение объекта')
def test_api_get_objects():
    with allure.step('Отправка запроса на получение списка всех объектов'):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200


@allure.title('Получение одного объекта по его ID')
@allure.feature('Метод GET')
@allure.story('Получение объекта')
def test_api_get_the_object(new_post_id):
    with allure.step(f'Отправка запроса на получение объекта с ID {new_post_id}'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200, 'Wrong status code'
    with allure.step(f'ID полученного объекта равен {new_post_id}'):
        assert response.json()['id'] == new_post_id, 'Wrong id'


@allure.title('Создание нового объекта')
@allure.feature('Метод POST')
@allure.story('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('body', [{"name": "Apple_1", "data": {"color": "red", "size": "small"}},
                                  {"name": "Apple_2", "data": {"color": "yellow", "size": "medium"}},
                                  {"name": "Apple_3", "data": {"color": "green", "size": "big"}}])
def test_api_add_post(body):
    with allure.step('Подготовка тестовых данных для запроса'):
        headers = {"Content-Type": "application/json"}
    with allure.step('Отправка запроса на создание объекта'):
        response = requests.post('http://objapi.course.qa-practice.com/object',
                                 json=body,
                                 headers=headers)
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200, 'Wrong status code'
    with allure.step('Параметр "Name" нового объекта соответствует запросу'):
        assert response.json()['name'] == body['name'], 'Wrong name'
    with allure.step('Параметр "Color" нового объекта соответствует запросу'):
        assert response.json()['data']['color'] == body['data']['color'], 'Wrong color'
    with allure.step('Параметр "Size" нового объекта соответствует запросу'):
        assert response.json()['data']['size'] == body['data']['size'], 'Wrong size'


@allure.title('Изменение всего объекта')
@allure.feature('Метод PUT')
@allure.story('Изменение объекта')
def test_api_put_the_post(new_post_id):
    with allure.step('Подготовка тестовых данных для запроса'):
        body = {"name": "My updated object",
                "data": {"color": "blue",
                         "size": "small"}}
        headers = {"Content-Type": "application/json"}
    with allure.step(f'Отправка запроса на изменение объекта с ID {new_post_id}'):
        response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                                json=body,
                                headers=headers)
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200, 'Wrong status code'
    with allure.step(f'ID изменённого объекта равен {new_post_id}'):
        assert response.json()['id'] == str(new_post_id), 'Wrong id'
    with allure.step('Параметр "Name" изменился корректно'):
        assert response.json()['name'] == 'My updated object', 'Wrong name'
    with allure.step('Параметр "Color" изменился корректно'):
        assert response.json()['data']['color'] == 'blue', 'Wrong color'
    with allure.step('Параметр "Size" изменился корректно'):
        assert response.json()['data']['size'] == 'small', 'Wrong size'


@allure.title('Частичное изменение объекта')
@allure.feature('Метод PATCH')
@allure.story('Изменение объекта')
def test_api_patch_the_post(new_post_id):
    with allure.step('Подготовка тестовых данных для запроса'):
        body = {"name": "My updated object",
                "data": {"color": "yellow",
                         "size": "small"}}
        headers = {"Content-Type": "application/json"}
    with allure.step(f'Отправка запроса на изменение объекта с ID {new_post_id}'):
        response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_post_id}',
                                  json=body,
                                  headers=headers)
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200, 'Wrong status code'
    with allure.step(f'ID изменённого объекта равен {new_post_id}'):
        assert response.json()['id'] == new_post_id, 'Wrong id'
    with allure.step('Параметр "Color" изменился корректно'):
        assert response.json()['data']['color'] == 'yellow', 'Wrong color'


@allure.title('Удаление объекта по его ID')
@allure.feature('Метод DELETE')
@allure.story('Удаление объекта')
@pytest.mark.medium
def test_api_delete_a_post(new_post_id):
    with allure.step(f'Отправка запроса на удаление объекта с ID {new_post_id}'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    with allure.step('Проверка, что получаем статус код 200'):
        assert response.status_code == 200, 'Wrong status code'

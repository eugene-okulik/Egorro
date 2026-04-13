import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    post_id = None
    headers = {"Content-Type": "application/json"}

    # @allure.step('Create new object')
    # def new_post_id(self):
    #     payload = {"name": "My object",
    #             "data": {"color": "red",
    #                      "size": "medium"}}
    #     self.response = requests.post(self.url,
    #                                   json=payload,
    #                                   headers=self.headers
    #                                   )
    #     self.json = self.response.json()
    #     post_id = self.json()['id']
    #     yield post_id
    #     requests.delete(f'{self.url}/{post_id}')

    @allure.step('Check response status code')
    def assert_status_code_is(self, code):
        print(f'{self.response.status_code} == {code}')
        assert self.response.status_code == code, 'Wrong status code'

    def assert_name_in_response_matches_payload(self, name):
        assert self.json['name'] == name, 'Name in response differs from the name in payload'

    def assert_color_in_response_matches_payload(self, color):
        assert self.json['data']['color'] == color, 'Color in response differs from the name in payload'

    def assert_size_in_response_matches_payload(self, size):
        assert self.json['data']['size'] == size, 'Size in response differs from the name in payload'

import requests
import allure
from endpoints.endpoint import Endpoint




class PostObject(Endpoint):


    @allure.step('Create new object')
    def post_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url,
                                      json=payload,
                                      headers=headers
                                      )
        self.json = self.response.json()
        return self.response

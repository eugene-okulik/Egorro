import requests
import allure
from endpoints.endpoint import Endpoint




class GetObject(Endpoint):


    @allure.step('Get object')
    def get_object(self, object_id=None, headers=None):
        headers = headers if headers else self.headers
        if object_id:
            self.response = requests.get(f'{self.url}/{object_id}', headers=headers)
        else:
            self.response = requests.get(self.url, headers=headers)
        self.json = self.response.json()
        return self.response

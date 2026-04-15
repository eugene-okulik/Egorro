import requests
import allure
from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Patch object')
    def patch_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{object_id}',
                                     json=payload,
                                     headers=headers
                                     )
        self.json = self.response.json()
        return self.response

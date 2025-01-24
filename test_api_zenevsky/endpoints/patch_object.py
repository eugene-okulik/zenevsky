import allure
import requests

from test_api_zenevsky.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Run "Patch object" request to patch an object')
    def patch_object(self, payload, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            url=f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response

import allure
import requests

from test_api_zenevsky.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Run "Update object" request to update an object')
    def update_object(self, payload, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response

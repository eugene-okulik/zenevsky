import allure
import requests

from test_api_zenevsky.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Run "Get object" request to get an object')
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/{object_id}',
            headers=headers
        )
        return self.response

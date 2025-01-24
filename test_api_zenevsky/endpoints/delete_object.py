import allure
import requests

from test_api_zenevsky.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Run "Delete object" request to delete an object')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f'{self.url}/{object_id}',
            headers=headers
        )
        return self.response

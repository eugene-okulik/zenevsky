import allure
import requests
import json

from test_api_zenevsky.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step('Run "Create object" request to create a new object')
    def create_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=self.url,
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.object_id = self.json['id']
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response

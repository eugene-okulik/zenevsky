import random
from locust import HttpUser, task


class ObjectUser(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            url='/object',
            json={"name": "test", "data": {"field_1": "value_1", "field_2": True}}
        )
        self.object_id = response.json()['id']

    @task(2)
    def get_all_objects(self):
        self.client.get(
            url='/object'
        )

    @task(5)
    def get_object(self):
        self.client.get(
            url=f'/object/{random.choice([1, 451, 452, 453])}'
        )

    @task(1)
    def create_object(self):
        self.client.post(
            url='/object',
            json={"name": "test", "data": {"field_1": "value_1", "field_2": True}}
        )

    @task(1)
    def update_object(self):
        self.client.put(
            url=f'/object/{self.object_id}',
            json={"name": "test", "data": {"field_1": "value_1", "field_2": True}}
        )

    @task(1)
    def patch_object(self):
        self.client.patch(
            url=f'/object/{self.object_id}',
            json={"name": "test", "data": {"field_1": "value_1", "field_2": True}}
        )

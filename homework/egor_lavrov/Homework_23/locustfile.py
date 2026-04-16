from locust import task, HttpUser


class ObjLocust(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get('',
                        headers={"Content-Type": "application/json"})

    @task(5)
    def get_one_objects(self):
        self.client.get('/1',
                        headers={"Content-Type": "application/json"})

    @task(1)
    def create_object(self):
        payload = {"name": "Apple_1", "data": {"color": "red", "size": "small"}}
        headers = {"Content-Type": "application/json"}
        response = self.client.post('',
                                    json=payload,
                                    headers=headers
                                    )
        obj_id = response.json()['id']
        self.client.delete(f'/{obj_id}',
                           json=payload,
                           headers=headers
                           )

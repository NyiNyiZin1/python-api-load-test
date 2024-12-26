from locust import HttpUser, task, between
import config
import random

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Time between tasks

    def on_start(self):
        keycloak_url = config.KEYCLOAK_URL
        data = {
            "client_id": config.KEYCLOAK_CLIENT_ID,
            "client_secret": config.KEYCLOAK_CLIENT_SECRET,
            "username": config.KEYCLOAK_USERNAME,
            "password": config.KEYCLOAK_PASSWORD,
            "grant_type": config.KEYCLOAK_GRANT_TYPE,
        }

        with self.client.post(keycloak_url, data=data, catch_response=True) as response:
            if response.status_code == 200:
                self.token = response.json()['access_token']
                self.headers = {'Authorization': f'Bearer {self.token}'}
            else:
                response.failure("Failed to obtain token")

    
    @task(10)  # Higher weight for critical endpoint
    def critical_endpoint(self):
        self.client.get(config.CRITICAL_ENDPOINT, headers=self.headers)

    @task
    def random_endpoint(self):
        endpoint = random.choice(config.API_ENDPOINTS)
        self.client.get(endpoint, headers=self.headers)

    

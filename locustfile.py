from locust import HttpUser, task, between


class RecargaUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 2)

    @task
    def calcular_recarga(self):
        self.client.post(
            "/calcular-recarga",
            json={
                "monto": 10000,
                "premium": False
            }
        )
import requests

BASE_URL = "http://127.0.0.1:8000"

class Test_1:
    def make_request(self, method: str, endpoint: str, **kwargs):
        """Универсальный метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response

    def start_test(self):
        pass

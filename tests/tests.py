import requests
from .server import Server

BASE_URL = "http://127.0.0.1:8000"

class Test_1:
    def make_request(self, method: str, endpoint: str, **kwargs):
        """Универсальный метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response

    def start_test(self):
        print("Тест 1")


if __name__ == "__main__":
    # Запускаем сервер перед тестами
    server = Server()
    server.start()

    # Тесты:
    test_1 = Test_1()
    test_1.start_test()

    # Останавливаем сервер после тестов
    server.stop()

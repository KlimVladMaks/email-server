import requests
import subprocess
import time
from .server import Server

BASE_URL = "http://127.0.0.1:8000"

class Test_1:
    # def start_server(self):
    #     """Запуск сервера"""
    #     print("Запуск сервера FastAPI...")
    #     server_process = subprocess.Popen(
    #         ["fastapi", "dev", "app/main.py"],
    #         stdout=subprocess.DEVNULL,
    #         stderr=subprocess.DEVNULL
    #     )
    #     print("Ожидание запуска сервера (5 секунд)...")
    #     time.sleep(5)
    #     return server_process

    def make_request(self, method: str, endpoint: str, **kwargs):
        """Универсальный метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response

    def start_test(self):
        server = Server()
        server.start()


if __name__ == "__main__":
    test = Test_1()
    test.start_test()

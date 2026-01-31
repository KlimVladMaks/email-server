from pathlib import Path
import subprocess
import os
import time
import requests


class Server:
    """
    Класс для запуска и остановки сервера.
    Можно использовать при написании тестов:
    - Перед началом выполнения теста запустить сервер через `start()`.
    - После выполнения тестов остановить сервер через `stop()`.
    """
    def __init__(self):
        # Путь к корню проекта
        self.project_root = Path(__file__).parent.parent
        # Путь к стартовому файлу main.py
        self.main_app = self.project_root / "app" / "main.py"
    
        # Процесс, в котором будет запущен сервер
        self.process = None
    
    def wait_for_server(self, host: str, port: int, timeout: int = 30) -> bool:
        """
        Метод для проверки доступности сервера.
        Если сервер работает, то возвращается True, если нет, то возвращается False.
        """
        start_time = time.time()
        url = f"http://{host}:{port}/"

        while time.time() - start_time < timeout:
            try:
                response = requests.get(url, timeout=2)

                # Если нужный ответ успешно получен, то возвращаем True
                if response.status_code == 200 and "email_server" in response.text:
                    return True
            
            # Если не удалось подключиться к серверу, то ждём и пробуем снова
            except (requests.ConnectionError, requests.Timeout):
                time.sleep(1)
            except requests.RequestException as e:
                print(f"Ошибка при проверке сервера: {e}")
                time.sleep(1)
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
                break
        
        # Если сервер так и не запустился, то возвращаем False
        return False
    
    def start(self):
        """Запуск сервера"""
        # Команда для запуска сервера
        command = [
            "uvicorn",
            "app.main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ]

        print("Запускаем сервер...")

        # Запускаем сервер в отдельном процессе
        self.process = subprocess.Popen(
            command,
            cwd=self.project_root,
            env={**os.environ, "VIRTUAL_ENV": str(self.project_root / ".venv")}
        )

        # Проверяем, что сервер работает корректно
        if self.wait_for_server("127.0.0.1", 8000):
            print("✓ Сервер запущен и работает корректно!")
        else:
            print("✗ Ошибка: сервер не запустился или работает некорректно")

    def stop(self):
        """Остановка сервера"""
        self.process.terminate()
        self.process.wait()
        print("Сервер остановлен")

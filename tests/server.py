from pathlib import Path
import subprocess
import os
import time


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

        # Запускаем сервер с отдельном процессе
        self.process = subprocess.Popen(
            command,
            cwd=self.project_root,
            env={**os.environ, "VIRTUAL_ENV": str(self.project_root / ".venv")}
        )

        time.sleep(3)

        if self.process.poll() is None:
            print("Сервер запущен")
        else:
            print("Ошибка при запуске сервера")

    def stop(self):
        """Остановка сервера"""
        self.process.terminate()
        self.process.wait()
        print("Сервер остановлен")

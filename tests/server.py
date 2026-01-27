from pathlib import Path
import subprocess
import os
import time


class Server:
    def __init__(self):
        # Определяем основные пути для запуска сервера:
        # Корневой путь проекта
        self.project_root = Path(__file__).parent.parent
        # Путь к main.py файлу
        self.main_app = self.project_root / "app" / "main.py"

        # Процесс, в котором будет запущен сервер
        self.process = None
    
    def start(self):
        """Запуск сервера"""
        # Команда для запуска uvicorn
        command = [
            "uvicorn",
            "app.main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ]

        print("Запускаем сервер...")

        # Запускаем процесс
        self.process = subprocess.Popen(
            command,
            cwd=self.project_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env={**os.environ, "VIRTUAL_ENV": str(self.project_root / ".venv")}
        )

        time.sleep(5)

        if self.process.poll() is None:
            print("Сервер запущен")
        else:
            stderr = self.process.stderr.read()
            print(f"Ошибка запуска сервера: {stderr}")

    def stop(self):
        """Остановка сервера"""
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("Сервер остановлен")

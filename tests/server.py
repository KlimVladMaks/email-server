from pathlib import Path


class Server:
    def __init__(self):
        # Определяем основные пути для запуска сервера:
        # Корневой путь проекта
        self.project_root = Path(__file__).parent.parent
        # Путь для активации venv
        self.venv_activate = self.project_root / ".venv" / "bin" / "activate"
        # Путь к main.py файлу
        self.main_app = self.project_root / "app" / "main.py"

        # Процесс, в котором будет запущен сервер
        self.process = None
    
    def start(self):
        print(self.main_app)

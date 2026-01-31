# Заметки

## Работа с `.venv`

```
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

## Работа с `requirements.txt`

```
pip install -r requirements.txt
```

## Запуск FastAPI

```
fastapi dev app/main.py
```

## Доступ к админ-панели

```
http://127.0.0.1:8000/admin/
```

## Запуск тестов

```
python -m tests.tests
```

## Работа с процессами uvicorn

```
# Найти все процессы uvicorn
pgrep -fl uvicorn

# Убить конкретный процесс
kill <id_процесса>

# Убить все процессы uvicorn
kill $(pgrep -f uvicorn)
```

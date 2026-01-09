from sqladmin.authentication import AuthenticationBackend
from fastapi import Request
from sqladmin import ModelView
from .models import User, Session


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Проверяем логин и пароль для доступа к админ-панели
        # (В перспективе можно брать данные администраторов из БД)
        if username == "admin" and password == "admin":
            request.session.update({"token": "admin-token"})
            return True
        return False
    
    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True
    
    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if token == "admin-token":
            return True
        return False


class UserAdmin(ModelView, model=User):
    """
    Модель для отображения пользователей в админ-панели
    """
    column_list = [User.id, User.username, User.is_active]
    column_searchable_list = [User.username]
    column_sortable_list = [User.id, User.username]
    column_details_exclude_list = [User.password]

    # Пагинация
    page_size = 20
    page_size_options = [10, 20, 50, 100]


class SessionAdmin(ModelView, model=Session):
    column_list = [Session.id, Session.user, Session.token]

    # Пагинация
    page_size = 20
    page_size_options = [10, 20, 50, 100]

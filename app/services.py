from app.repository import FakeUserRepository

class UserService:
    def __init__(self, repository=None):
        self.repo = repository or FakeUserRepository()

    def register_user(self, name, email, password):
        if not name or not email or not password:
            raise ValueError("Todos os campos são obrigatórios.")

        if self.repo.get_user_by_email(email):
            raise ValueError("E-mail já cadastrado.")

        user = {"name": name, "email": email, "password": password}
        self.repo.add_user(user)
        return user

    def login(self, email, password):
        user = self.repo.get_user_by_email(email)
        if not user or user["password"] != password:
            raise ValueError("Credenciais inválidas.")
        return True

import pytest
from app.services import UserService
from app.repository import FakeUserRepository

@pytest.fixture
def service():
    return UserService(FakeUserRepository())

def test_register_valid_user(service):
    user = service.register_user("Maria", "maria@email.com", "123")
    assert user["name"] == "Maria"

def test_register_existing_email(service):
    service.register_user("João", "joao@email.com", "abc")
    with pytest.raises(ValueError, match="E-mail já cadastrado."):
        service.register_user("Outro João", "joao@email.com", "xyz")

def test_login_success(service):
    service.register_user("Ana", "ana@email.com", "senha123")
    assert service.login("ana@email.com", "senha123") is True

def test_login_fail_wrong_password(service):
    service.register_user("Pedro", "pedro@email.com", "senha")
    with pytest.raises(ValueError, match="Credenciais inválidas."):
        service.login("pedro@email.com", "errado")

def test_register_missing_fields(service):
    with pytest.raises(ValueError, match="Todos os campos são obrigatórios."):
        service.register_user("", "email@email.com", "senha")

#Para rodar os testes:

#python -m venv venv
#.\venv\Scripts\activate
#pip install -r requirements.txt
#pytest 
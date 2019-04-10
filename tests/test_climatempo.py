from climatempo_api.climatempo import Climatempo
from climatempo_api.climatempo import BASE_URL, VERSION
import os


def test_criar_climatempo():
    climatempo = Climatempo("***")
    assert climatempo is not None


def test_formatar_endpoint():
    climatempo = Climatempo("***")
    assert climatempo._formatar_endpoint("/test/") == f'{BASE_URL}{VERSION}/test/?token=***'


def test_token():
    assert os.getenv("CLIMATEMPO_TOKEN") is not None


def test_busca_cidade_id():
    climatempo = Climatempo()
    response = climatempo.busca_cidade_ID(3477)
    assert response['id'] == 3477, "ID da cidade de SP"


def test_busca_cidade_id():
    climatempo = Climatempo()
    response = climatempo.busca_cidade_nome("São Paulo", "SP")
    assert response[0]['id'] == 3477, "ID da cidade de SP"

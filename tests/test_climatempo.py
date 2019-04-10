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


def test_busca_cidade_nome():
    climatempo = Climatempo()
    response = climatempo.busca_cidade_nome(3477)

    assert response['id'] == 3477, "ID da cidade de SP"

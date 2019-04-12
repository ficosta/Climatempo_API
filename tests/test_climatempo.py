from climatempo_api.climatempo import Climatempo, BASE_URL, VERSION
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


def test_busca_cidade_nome():
    climatempo = Climatempo()
    response = climatempo.busca_cidade_nome("São Paulo", "SP")
    assert response[0]['id'] == 3477, "ID da cidade de SP"


# def test_chuva_climatica():
#     climatempo = Climatempo()
#     response = climatempo.chuva_climatica(3477)
#     assert response['id'] == 3477, "ID da cidade de SP"


def test_previsao_15_dias():
    climatempo = Climatempo()
    response = climatempo.previsao_15_dias(3477)
    assert response['id'] == 3477, "ID da cidade de SP"


def previsao_72_horas():
    climatempo = Climatempo()
    response = climatempo.previsao_72_horas(3477)
    assert response['id'] == 3477, "ID da cidade de SP"


def tempo_momento():
    climatempo = Climatempo()
    response = climatempo.tempo_momento(3477)
    assert response['id'] == 3477, "ID da cidade de SP"

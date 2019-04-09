from climatempo_api.climatempo import Climatempo
from climatempo_api.climatempo import BASE_URL, VERSION


def test_criar_climatempo():
    climatempo = Climatempo()
    assert climatempo is not None


def test_formatar_endpoint():
    climatempo = Climatempo("***")
    assert climatempo._formatar_endpoint("/test/") == f'{BASE_URL}{VERSION}/test/?token=***'

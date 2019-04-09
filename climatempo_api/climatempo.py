import requests

BASE_URL = "http://apiadvisor.climatempo.com.br/api"
VERSION = "/v1"


class Climatempo():
    def __init__(self, token: str):
        self.token = token

    # === Climate ---
    def chuva_climatica(self, id: int):
        """
        Chuva climatica por ID

        :param id: ID da cidade
        :return: Dicionario com os dados
        """
        endpoint = self._formatar_endpoint(f"/climate/rain/locale/{id}")
        return self._requisitar_dados(endpoint)

    # --- Forecast ---
    def previsao_15_dias(self):
        return NotImplemented

    def previsao_72_horas(self):
        return NotImplemented

    # --- Locale ---
    def busca_cidade_ID(self, id: int):
        return NotImplemented

    def busca_cidade_nome(self, nome: str = "", estado: str = ""):
        return NotImplemented

    # --- Weather ---
    def tempo_momento(self, id: int):
        return NotImplemented

    def _formatar_endpoint(self, endpoint: str) -> str:
        return f'{BASE_URL}{VERSION}{endpoint}?token={self.token}'

    def _requisitar_dados(self, endpoint: str) -> dict:
        return requests.get(endpoint).json()

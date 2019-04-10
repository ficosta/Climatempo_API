import requests
from . import CLIMATEMPO_TOKEN

BASE_URL = "http://apiadvisor.climatempo.com.br/api"
VERSION = "/v1"


class Climatempo():
    def __init__(self, token: str = CLIMATEMPO_TOKEN):
        self.token = token

    # === Climate ---
    def chuva_climatica(self, id: int):
        """
        Retorna a chuva climatica da cidade fornecida por ID

        :param id: ID da cidade
        :return: Dicionario com os dados
        """
        endpoint = self._formatar_endpoint(f"/climate/rain/locale/{id}")
        return self._requisitar_dados(endpoint)

    # --- Forecast ---
    def previsao_15_dias(self, id: int):
        """
        Retorna a previão para 15 dias da cidade fornecida por ID.

        :param id: ID da cidade
        :return: Dicionario com os dados
        """
        endpoint = self._formatar_endpoint(f"/forecast/locale/{id}/days/15")
        return self._requisitar_dados(endpoint)

    def previsao_72_horas(self, id: int):
        """
        Retorna a previsão para 72 horas da cidade fornecida por ID.

        :param id: ID da cidade
        :return: Dicionario com os dados
        """
        endpoint = self._formatar_endpoint(f"/forecast/locale/{id}/hours/72")
        return self._requisitar_dados(endpoint)

    # --- Locale ---
    def busca_cidade_ID(self, id: int):
        """
        Retorna os dados da cidade para o ID especificado.

        :param id: ID da cidade
        :return: Dicionario com os dados
        """

        endpoint = self._formatar_endpoint(f"/locale/city/{id}")
        return self._requisitar_dados(endpoint)

    def busca_cidade_nome(self, cidade: str = "", estado: str = ""):
        """
        Retorna os dados de uma cidade para a cidade e o estado fornecido.

        :param cidade:
        :param estado:
        :return: Dicionario com os dados
        """

        endpoint = self._formatar_endpoint(f"/locale/city?name={cidade}&state={estado}")
        return self._requisitar_dados(endpoint)

    # --- Weather ---
    def tempo_momento(self, id: int):
        """
        Retorna o tempo no momento para o ID especificado.

        :param id: ID da cidade
        :return: Dicionario com os dados
        """

        endpoint = self._formatar_endpoint(f"/weather/locale/{id}/current")
        return self._requisitar_dados(endpoint)

    def _formatar_endpoint(self, endpoint: str) -> str:
        return f'{BASE_URL}{VERSION}{endpoint}?token={self.token}'

    def _requisitar_dados(self, endpoint: str) -> dict:
        return requests.get(endpoint).json()
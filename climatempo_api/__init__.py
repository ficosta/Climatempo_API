import os

CLIMATEMPO_TOKEN = os.environ.get('CLIMATEMPO_TOKEN', None)


class APIKeyMissingError(Exception):
    pass


if CLIMATEMPO_TOKEN is None:
    raise APIKeyMissingError(
        "Todos as chamadas necessitam de um token."
        "Gere seu token em: advisor.climatempo.com.br"
    )

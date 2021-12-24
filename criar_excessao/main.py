class ErroPerso(Exception):
    pass


def testar():
    raise ErroPerso('errado')

try:
    testar()
except ErroPerso as erro:
    print(f'Erro: {erro}')
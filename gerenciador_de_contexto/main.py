from contextlib import contextmanager
@contextmanager
def abrir(arquivo, modo):
    try:
        print('Arquivo aberto')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()
        print('Arquivo fechado')

with abrir('dados.txt','w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')
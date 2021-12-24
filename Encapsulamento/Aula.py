'''
public, protected, private
'_'(antes da variavel) protected -->  não é recomendavel ser acessado
'__'(antes da variavel) private --> não pode ser acessado externamente
    a não ser assim: (_NOMECLASSE__nomeatributo)
'''

class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def InserirCliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def ListarClientes(self):
        for id ,cliente in self.dados['clientes'].items():
            print(f'{id:-<10}{cliente}')
    def ApagaCliente(self, id):
        del self.dados['clientes'][id]

bd = BaseDeDados()
bd.InserirCliente(1,'vitor')
bd.InserirCliente(2,'josué')
bd.InserirCliente(3,'lucas')
print()






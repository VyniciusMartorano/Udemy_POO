class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        print(f'CLIENTE: {self.nome}')
        print(f'Endereço:')
        print(f'{"Estado":<15}{"Cidade"}')
        for endereco in self.enderecos:
            print(f'{endereco.estado:-<15}{endereco.cidade}')

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, estado, cidade):
        self.cidade = cidade
        self.estado = estado
    def __del__(self):
        print(f'{self.estado}/{self.cidade} FOI APAGADO')
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError('Tipo inválido')

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa(18, 'vynicius')





'''
p1 = Pessoa('vitor','Vynicius')
print(p1)  #saida: Pessoa(nome='Vitor', sobrenome='Vynicius')
print(p1.nome)  #saida: 'vitor'
print(p1.sobrenome)  #saida: 'vynicius'
print(p1.nome_completo())   #saida: 'vitor vynicius'
'''


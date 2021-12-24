# Setter = Configurando um valor
# Getter = Obter um valor

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        print('init executado')

    @property
    def nome(self):
        print('Getter foi execultado')
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Setter foi executado!')
        self._nome = nome.replace(' ','')



p1 = Pessoa('     @  vitor')
print(p1.nome)
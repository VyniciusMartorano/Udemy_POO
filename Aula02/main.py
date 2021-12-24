
class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


    def aumento(self, percentual):
        aum = self._preço + self._preço * (percentual / 100)
        print(f'{self._nome} com aumento de {percentual}% fica R${aum}')
    #getter
    @property
    def preço(self):
        return self._preço
    #setter
    @preço.setter
    def preço(self,valor):
        self._preço = valor

    #getter
    @property
    def nome(self):
        return self._nome
    #setter
    @nome.setter
    def nome(self,valor):
        self._nome = valor.lower()




p1 = Produto('Geladeira',8700)

print(p1.nome)
p1.aumento(30)

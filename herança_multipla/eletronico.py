class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já esta ligado.')
        else:
            self._ligado = True
            print(f'Você acaba de ligar o aparelho {self._nome}')
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'Voce acaba de desligar o aparelho {self._nome}')
        else:
            return
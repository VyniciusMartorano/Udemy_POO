from datetime import datetime
ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
class Pessoa:
    def __init__(self, nome = 'fulano', idade = 18, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já esta falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    def parar_falar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar.')
            self.falando = False
            return
        print(f'{self.nome} não esta falando no momento')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja está comendo')
            return
        elif self.falando:
            print(f'{self.nome} está falando e por isso não pode comer')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return
        elif self.comendo:
            print(f'{self.nome} parou de comer!')
            self.comendo = False
    def ano_nascimento(self):
        nasc = ano_atual - self.idade
        print(f'O ano do nascimento de {self.nome} foi {nasc}')
        return
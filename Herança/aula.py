import função_cor


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__   #Saber o nome da classe
    def falar(self):
        print(f'{self.nome_classe} está Falando.....')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} está comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando...')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'
    def falar(self):
        Pessoa.falar()
        Cliente.falar()
        print(f'{self.nome_completo}')





    def xx(self, coloração):
        super().falar()   #executa o metodo da super classe primeiro
        from função_cor import cor
        print(f'{cor(coloração)}cliente VIP {cor("white")}tem o previlegio{cor("cyan")} de falar colorido')



    def comprar(self):
        print(f'cliente VIP{função_cor.cor("green")} Tem o privilegio de comprar mais coisas')
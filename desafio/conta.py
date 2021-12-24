from abc import abstractmethod, ABC

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def detalhes(self):
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')


    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupança(Conta):
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            self.detalhes()
        else:
            print('Saldo insuficiente')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) > valor:
            self.saldo -= valor
            self.detalhes()
        else:
            print('Saldo insuficiente')


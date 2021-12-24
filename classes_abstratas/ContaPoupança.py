from classes_abstratas.classes.conta import Conta
class ContaPoupança(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente para saque.')
        else:
            self.saldo = self.saldo - valor
            print(f'Saque de R${valor} realizado!\nNovo Saldo: {self.saldo}')
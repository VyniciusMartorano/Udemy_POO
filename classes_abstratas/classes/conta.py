from abc import ABC, abstractmethod

class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        if not  isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numérico')
        self._saldo += valor
        print(f'Deposito de R${valor} realizado.\nNovo saldo: {self._saldo}')

    def detalhes(self):
        print(f'Agência: {self._agencia}'
              f'\nConta: {self._conta}'
              f'\nSaldo: R${self._saldo}')


    @abstractmethod
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numérico')
        self._saldo -= valor
        print(f'Novo saldo: {self._saldo}')





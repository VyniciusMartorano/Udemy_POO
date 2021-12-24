from desafio.banco import Banco
from desafio.conta import ContaPoupança, ContaCorrente
from desafio.cliente import Cliente

banco = Banco()

cliente1 = Cliente('vynicius martorano', 18)
conta1 = ContaCorrente(1111, 254116, 0)

cliente1.inserir_conta(conta1)
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
if banco.autenticar(cliente1):
    conta1.sacar(3)
else:
    print('saldo insuficiente')

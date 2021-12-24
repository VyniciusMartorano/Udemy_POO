from Herança.aula import *
pessoa = Pessoa('vitor',18)
aluno = Aluno('italo',16)
cliente = Cliente('josefa',35)
cVIP = ClienteVIP('Felipe',6,'Roblox')
'''pessoa.falar()
aluno.falar()
cliente.falar()
aluno.estudar()
cliente.comprar()'''

#SAIDA
#Pessoa está Falando.....
#Aluno está Falando.....
#Cliente está Falando.....
#Aluno está estudando...
#Cliente está comprando...
print(cVIP.nome_completo)
cVIP.xx('black')
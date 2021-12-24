from atividade.pessoa import Pessoa
p1 = Pessoa.por_ano_nascimento('vitor',2003)
print(p1.idade)
print(Pessoa.gera_id())
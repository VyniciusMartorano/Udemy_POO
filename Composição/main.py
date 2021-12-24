from Composição.aula import Cliente
c = Cliente('vitor',18)
c2 = Cliente('José',24)

c.insere_endereco('RN','Natal')
c.insere_endereco('DF','Brasilia')
c.insere_endereco('SP','São Paulo')
c.insere_endereco('RJ','Rio de Janeiro')
c.lista_enderecos()
del c

c2.insere_endereco('MG','Belo horizonte')
c2.insere_endereco('CE','Fortaleza')
c2.insere_endereco('PE','Recife')
c2.lista_enderecos()
del c2




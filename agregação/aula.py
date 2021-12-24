from agregação.classes import CarrinhoDeCompras, Produto
car = CarrinhoDeCompras()
pro = Produto()

p1 = pro.criaproduto('Tv',1300)
p2 = pro.criaproduto('carrinho',120)
p3 = pro.criaproduto('ps5',4999)
p4 = pro.criaproduto('geladeira',3200)

car.inserir(p1)
car.inserir(p2)
car.inserir(p3)
car.inserir(p4)
car.inserir(p1)

car.mostraprodutos()
car.somacarrinho()




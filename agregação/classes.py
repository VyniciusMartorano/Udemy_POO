
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir(self, produto):
        self.produtos.append(produto)

    def mostraprodutos(self):
        print(f'{"Produto":<25}{"Valor"}')
        for produto, valor in self.produtos:
            print(f'{produto:-<25}>R${valor}')
    def somacarrinho(self):
        soma = 0
        for nome, produto in self.produtos:
            soma += produto
        print(f'A soma de todos os produtos do carrinho é R${soma}')


class Produto:
    def criaproduto(self, nome, valor):
        formatado = nome.title()
        produto = [formatado,valor]
        return produto




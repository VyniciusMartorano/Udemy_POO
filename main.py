class A:
    def falar(self):
        print('Falando... Estou em A')

class B(A):
    def falar(self):
        print('Falando... Estou em B')

class C(A):
    def falar(self):
        print('Falando... Estou em C')

class D(C, B):
    pass


d = D()
d.falar() #saida: estou em C pq o  C vem primeiro na herança do D
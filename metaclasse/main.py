'''
EM PYTHON TUDO É UM OBJETO: incluindo classes
metaclasses são as 'classes' que criam classes.
type é uma metaclasse
'''

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)

        if 'b_fala' not in namespace:
            print(f'oi, voce precisa criar o metodo b_fala em {name}')

        else:
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um método, não atributo')

        return type.__new__(mcs, name, bases, namespace)
class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'valor'

    pass
    def seila(self):
        pass



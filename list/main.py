
class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0


    def add(self, valor):
        self.__items.append(valor)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('vitor')
    lista.add('italo')

    lista[2] = 'juliana'
    for i in lista:
        print(i)
from herança_multipla.eletronico import Eletronico
from herança_multipla.log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if self._ligado:
            if self._conectado:
                erro = f'{self._nome} já está conectado'
                self.log_error(erro)
                print(erro)
            else:
                self._conectado = True
                info = f'{self._nome} acaba de se conectar a internet.'
                self.log_info(info)
                print(info)
        else:
            erro = f'{self._nome} está desligado e não consegue se conectar a internet'
            self.log_error(erro)
            print(erro)
    def desconectar(self):
        if self._ligado:
            if self._conectado:
                info = f'Você acaba de desconectar {self._nome}.'
                print(info)
                self.log_info(info)
                self._conectado = False
            else:
                erro = 'Você ja está desconectado'
                print(erro)
                self.log_error(erro)
        else:
            erro = f'{self._nome} está desligado e não consegue se desconectar da internet.'
            print(erro)

    def status(self):
        print(f'STATUS {self._nome}\nLIGADO: {self._ligado}\nCONECTADO: {self._conectado}')


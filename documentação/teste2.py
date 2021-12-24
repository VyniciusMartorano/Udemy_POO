from documentação import teste
from typing import Union
'''
                            #A função retorna float
def função(p1: float, p2: int, p3: str) -> float:    #dizer pro desenvolvedor qual a classe que a variavel tem
    return 10.10                                     # que estar,
'''
                    #dizer que pode retornar 2 valores
def função(name) -> Union[dict, list]:
    return ['vitor']

print(função(''))
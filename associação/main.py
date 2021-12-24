from associação.classes import Escritor
from associação.classes import Caneta
from associação.classes import MaquinaDeEscrever

escritor = Escritor('vynicius')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever



escritor.ferramenta = maquina
escritor.ferramenta.escrever('')
maquina.escrever('')
print(caneta.marca)
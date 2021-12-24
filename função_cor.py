def cor(coloração):
    if isinstance(coloração, str):
        escolha = coloração.lower()
        if escolha == 'stop':
            return '\033[m'
        elif escolha == 'red':
            return '\033[31m'
        elif escolha == 'black':
            return '\033[1;30m'
        elif escolha == 'green':
            return '\033[1;32m'
        elif escolha == 'yellow':
            return '\033[1;33m'
        elif escolha == 'blue':
            return '\033[1;34m'
        elif escolha == 'cyan':
            return '\033[1;36m'
        elif escolha == 'white':
            return '\033[1;97m'
    else:
        print('Cor inválida!')


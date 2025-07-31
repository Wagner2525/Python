from time import sleep

def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cores[0], end='')
    sleep(1)

def ajuda(comando):
    título(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')
    sleep(2)

cores = (
'\033[m', # 0 - sem cores
'\033[0;30;41m', # 1 - vermelho
'\033[0;30;42m', # 2 - verde
'\033[0;30;43m', # 3 - amarelo
'\033[0;30;44m', # 4 - azul
'\033[0;30;45m', # 5 - roxo
'\033[7;30m' # 6 - branco
)


# Main
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP ', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
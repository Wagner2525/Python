from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

pasta = os.path.dirname(__file__)  
aqr = os.path.join(pasta, 'cadastro_pessoas.txt')

if not arquivoExiste(aqr):
    criarArquivo(aqr)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(aqr)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(aqr, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
        sleep(2)
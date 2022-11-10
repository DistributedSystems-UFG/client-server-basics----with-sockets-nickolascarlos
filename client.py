from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print('''
OPERAÇÕES SUPORTADAS:
* TO_LOWER
* TO_UPPER
* TO_CAPITALIZED
* TO_ALTERNATED
* TO_NUMBERIZED
''')

while True:
    operacao = input('Operação> ')
    if operacao.upper() == 'QUIT':
        break

    texto = input('Texto> ')

    s.send(str.encode(f'{operacao.upper()}~{texto}')) # Constrói e envia a mensagem para o servidor
    resposta = bytes.decode(s.recv(1024))             # Aguarda a resposta do servidor
    print(f'\nRESPOSTA: {resposta}\n')

s.close()

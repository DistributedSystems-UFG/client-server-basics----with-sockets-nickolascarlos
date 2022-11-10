from socket  import *
from constCS import *
from processadorMensagem import processaMensagem

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(1)
print('Aguardando conexão...')
conn, addr = s.accept()
print(f'Conexão estabelecida: {addr}\n')

while data := conn.recv(1024):
  message = bytes.decode(data)
  result = processaMensagem(message)

  print('--- SOLICITAÇÃO RECEBIDA ---')
  print(f'MENSAGEM: {message}')
  print('--- --- --- ---- --- --- ---\n')
  
  conn.send(str.encode(result))

conn.close()

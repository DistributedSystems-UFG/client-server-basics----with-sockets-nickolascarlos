# Serviço de Processamento de Texto

{LINK PARA O VÍDEO DEMONSTRATIVO}

## Descrição do Sistema

O sistema implementado visa ao processamento de strings e oferece, para tal finalidade, cinco operações diferentes:

|    Operação    |                                  Descrição                                  |
|:--------------:|:---------------------------------------------------------------------------:|
|    TO_LOWER    |               Converte todo o texto para caracteres minúsculos              |
|    TO_UPPER    |               Converte todo o texto para caracteres maiúsculos              |
| TO_CAPITALIZED |     Converte o caractere inicial de cada uma das palavras para maiúsculo    |
|  TO_ALTERNATED | Converte o texto para caracteres que alternam entre maiúsculos e minúsculos |
|  TO_NUMBERIZED |    Converte algumas letras do texto para números visualmente semelhantes    |

A interação entre o cliente e servidor consiste no envio, por parte do cliente, de uma mensagem estruturada (contendo a operação desejada e o texto a ser processado) ao servidor, o qual, por sua vez, fará o processamento do texto e o enviará para o cliente.

### Estrutura da mensagem
A mensagem enviada pelo cliente ao servidor deve seguir o seguinte padrão: ```OPERAÇÃO~TEXTO```, onde OPERAÇÃO é alguma das operações listadas logo acima e TEXTO é um texto qualquer para ser processado. Caso alguma operação não listada seja especificada, o servidor retornará um erro.

### Funcionamento dos scripts

#### server.py

O script do servidor, basicamente, segue o seguinte fluxo:

0. Abre um socket
1. Aguarda e aceita a conexão de um cliente
2. Aguarda o recebimento de uma mensagem
3. Processa a mensagem recebida, através da função processaMensagem
4. Envia para o cliente o texto resultante do processamento
5. Volta ao passo 2 e repete até o cliente fechar a conexão

#### client.py

O script do cliente conecta-se ao servidor especificado no arquivo constCS.py, imprime na tela as operações suportadas e, então, segue o seguinte fluxo:

0. Solicita ao usuário a operação desejada
1. Solicita ao usuário o texto a ser processado
2. Monta a mensagem, concatenando a operação e o texto separados por um ```~```
3. Envia a mensagem ao servidor
4. Aguarda a resposta do servidor
5. Imprime a resposta do servidor
6. Volta ao passo 0 e repete até o usuário sair do script

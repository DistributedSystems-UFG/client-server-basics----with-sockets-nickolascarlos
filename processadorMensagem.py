# Recebe mensagem, retorna texto processado
def processaMensagem(mensagem: str) -> str:
  # Estrutura da mensagem:
  # OPERAÇÃO~TEXTO
  # Suporte a 5 operações:
  # TO_LOWER, TO_UPPER, TO_CAPITALIZED, TO_ALTERNATED, TO_NUMBERIZED

  operacao, texto = mensagem.split('~')

  match operacao:
    case 'TO_UPPER':
      return texto.upper()
    case 'TO_LOWER':
      return texto.lower()
    case 'TO_CAPITALIZED':
      return texto.title()
    case 'TO_ALTERNATED':
      return ''.join([c.upper() if i % 2 == 0 else c.lower() for (i, c) in enumerate(texto)])
    case 'TO_NUMBERIZED':
      return texto.replace('a', '4').replace('A', '4')\
                  .replace('e', '3').replace('E', '3')\
                  .replace('i', '1').replace('I', '1')\
                  .replace('o', '0').replace('O', '0')\
                  .replace('t', '7').replace('T', '7')\
                  .replace('s', '5').replace('S', '5')
    case _:
      return 'ERRO: OPERAÇÃO NÃO SUPORTADA!'
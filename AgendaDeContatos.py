def cadastrar_contato(id):
  global id_global, lista_contatos
  id_global += 1
  contato = {}

  print('\n-------------------  MENU CADASTRAR CONTATO  --------------------')
  contato['id'] = id_global
  print(f'Id do contato: {id_global}')
  contato['nome'] = input('Digite o nome do contato: ')
  contato['atividade'] = input('Digite a atividade do contato: ')
  contato['telefone'] = input('Digite o telefone do contato: ')
  lista_contatos.append(contato.copy())
  print('Contato cadastrado com sucesso!')

def consultar_contatos():
  while True:
    try:
      print('\n-------------------  MENU CONSULTAR CONTATOS  --------------------')
      print('1 - Consultar Todos')
      print('2 - Consultar por Id')
      print('3 - Consultar por Atividade')
      print('4 - Retornar ao menu principal\n')
      opcao = int(input('O que deseja fazer? '))
      match(opcao):
        case 1:
          print('\n-------------------  LISTA COM TODOS OS CONTATOS  --------------------')
          for i in range(len(lista_contatos)):
            print(f'Id: {lista_contatos[i]["id"]}')
            print(f'Nome: {lista_contatos[i]["nome"]}')
            print(f'Atividade: {lista_contatos[i]["atividade"]}')
            print(f'Telefone: {lista_contatos[i]["telefone"]}')
            print()
        case 2:
          while True:
            encontrado = 0
            try:
              id = int(input('Informe o ID do contato? '))
              for values in lista_contatos:
                if values['id'] == id:
                  print('\n-------------------  CONTATO ENCONTRADO  --------------------')
                  print(f'Id: {values["id"]}')
                  print(f'Nome: {values["nome"]}')
                  print(f'Atividade: {values["atividade"]}')
                  print(f'Telefone: {values["telefone"]}')
                  encontrado = 1
                  break
              if encontrado == 0:
                  print('\n-------------------  NENHUM CONTATO ENCONTRADO  --------------------')
                  print('Tente novamente!\n')
              break
            except:
              print('ID inválido. Tente novamente.\n')
        case 3:
          while True:
            encontrado = 0
            listaTemp = []
            try:
              atividade = input('Informe a atividade? ').lower().strip()
              for values in lista_contatos:
                if values['atividade'].lower().strip() == atividade:
                  listaTemp.append(values)
                  encontrado = 1
              if encontrado == 0:
                  print('\n-------------------  NENHUM CONTATO ENCONTRADO  --------------------')
                  print('Tente novamente!\n')
              else:
                print('\n---------------  LISTA DOS CONTATOS ENCONTRADOS  ---------------')
                for contato_encontrado in listaTemp:
                  print(f'Id: {contato_encontrado["id"]}')
                  print(f'Nome: {contato_encontrado["nome"]}')
                  print(f'Atividade: {contato_encontrado["atividade"]}')
                  print(f'Telefone: {contato_encontrado["telefone"]}')
                  print()
              break
            except:
              print('Atividade inválida. Tente novamente.\n')
        case 4:
          return
        case _: #caso o cliente não responda 1, 2 ou 3 o laço reinicia
          print('Opção inválida. Tente novamente.\n')
    except:
      print('Entrada inválida. Tente novamente.\n')

def remover_contato():
  while True:
    encontrado = 0
    try:
      id = int(input('Informe o ID do contato a ser excluído? '))
      for values in lista_contatos:
        if values['id'] == id:
          lista_contatos.remove(values)
          print('\n-------------------  CONTATO REMOVIDO  --------------------')
          encontrado = 1
          break
      if encontrado == 0:
                  print('\n-------------------  NENHUM CONTATO ENCONTRADO  --------------------')
                  print('Tente novamente!\n')
      break
    except:
      print('ID inválido. Tente novamente.\n')




###### Programa principal ######
id_global = 5535667
lista_contatos = []
print('-------   Bem vindo a lista de contatos de Charles Silva da Silva   -------\n')

while True:
  print('\n-------------------  MENU PRINCIPAL  --------------------')
  print('1 - Cadastrar contato')
  print('2 - Consultar contato (s)')
  print('3 - Remover contato')
  print('4 - Encerrar Programa\n')

  match(input('O que deseja fazer? ').strip()):
    case '1':
      cadastrar_contato(id_global)
    case '2':
      consultar_contatos()
    case '3':
      remover_contato()
    case '4':
      break
    case _: #caso o cliente não responda 1, 2, 3 ou 4 o laço reinicia
      print('Opção inválida. Tente novamente.\n')

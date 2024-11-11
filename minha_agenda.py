# -- início das funções --

def adicionarContato(contatos,nome_contato, telefone_contato,email_contato):
  contato = {"nome": nome_contato, "telefone":telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)
  print(f"\nO contato: {nome_contato} - foi adicionado com sucesso!")

  return

def listarContatos(contatos):
  print("\nMeus contatos: ")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "★" if contato["favorito"] else " "
    print(f"\n{indice}. Contato: {contato['nome']} - Favorito: [{favorito}]")
    print(f"Telefone: {contato['telefone']} | Email: {contato['email']}")

  return

def atualizarContato(contatos, indice_contato ,nome_contato, telefone_contato, email_contato):
  # ajustando o indice para corresponder ao indice da lista que inicar com 0.
  indice_ajustado = indice_contato - 1

  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    contatos[indice_ajustado]["nome"] = nome_contato
    contatos[indice_ajustado]["telefone"] = telefone_contato
    contatos[indice_ajustado]["email"] = email_contato

    print(f"\nO Contato: {nome_contato} - foi atualizado com sucesso!")
  else:
    print("O índice do contato informado não existe na lista. Favor informar um número correspondente a lista de contatos!")

  return

def favoritarContato(contatos, indice_contato):
  indice_ajustado = indice_contato - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    
    #verificando se o contato já é favorito
    is_favorito = contatos[indice_ajustado]["favorito"]

    if is_favorito:
      print(f"\n Contato: {contatos[indice_ajustado]['nome']} - Favorito: [★] ")
      escolha = input("Deseja remover de favoritos? 1. SIM 2. NÃO: ")
      if escolha == "1":
        contatos[indice_ajustado]["favorito"] = False
    else:
      print(f"\n Contato: {contatos[indice_ajustado]['nome']} - Favorito: [ ] ")
      escolha = input("Deseja adicionar aos favoritos? 1. SIM 2. NÃO: ")
      if escolha == "1":
        contatos[indice_ajustado]["favorito"] = True  
  return

def listarFavoritos(contatos):
  contatos_favoritos = 0
  print("\nMeus Contatos Favoritos: ")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      print(f"\n{indice}. Contato: {contato['nome']} Favorito: [★]")
      print(f"Telefone: {contato['telefone']} | Email: {contato['email']}")
      contatos_favoritos += 1
 
  if contatos_favoritos <= 0:
    print("\n--- Não há contatos favoritos em sua agenda!")
    return

  return

def deletarContato(contatos, indice_contato):
  indice_ajustado = indice_contato - 1
  contatos.remove(contatos[indice_ajustado])
  print("\n Contato excluído! ")
  return

# -- fim das funções --
contatos = [{"nome":"Jose", "telefone":"61986111-9666","email":"jose@gmail.com", "favorito":False}]

print("\nBem vindo vindo a Minha Agenda!")

while True:
  print("\nEscolha uma das opções abaixo:")
  print("1 - Adicionar contato")
  print("2 - Ver contato")
  print("3 - Atualizar contato")
  print("4 - Adicionar/Remover contato de favorito")
  print("5 - Listar favoritos")
  print("6 - Deletar contato")
  print("7 - Sair")

  escolha = input("Digite a opção desejada: ")
  if escolha == "1":
    nome_contato = input("Digite o nome do novo contato: ")
    telefone_contato = input("Digite o telefone do novo contato: ")
    email_contato = input("Digite o email do novo contato: ")
    adicionarContato(contatos, nome_contato, telefone_contato, email_contato)

    print(contatos)
  
  elif escolha == "2":
    listarContatos(contatos)

  elif escolha == "3":
    listarContatos(contatos)

    # -- Entrada de dados
    indice_contato = int(input("\nDigite o número do contato que deseja atualizar: "))
    nome_contato = input("Informe novo NOME do contato: ")
    telefone_contato = input("Informe novo TELEFONE do contato: ")
    email_contato = input("Informe novo E-MAIL do contato: ")

    atualizarContato(contatos, indice_contato, nome_contato, telefone_contato, email_contato)

  elif escolha == "4":
    listarContatos(contatos)

    indice_contato = int(input("\nDigite o número do contato que deseja Adicionar ou Remover de Favoritos: "))
    favoritarContato(contatos, indice_contato)

    listarContatos(contatos)

  elif escolha == "5":

    listarFavoritos(contatos)
  
  elif escolha == "6":
    listarContatos(contatos)
    if len(contatos) > 0:
      indice_contato = int(input("\nInforme o número do contato que deseja excluir: "))
      deletarContato(contatos,indice_contato)
      listarContatos(contatos)
    else:
      print("\n-- Lista de contatos vazia! ---")

  elif escolha == "7":
    break
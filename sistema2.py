
# Sistema gerenciador de nomes
nomes=[]

while True:
    print("=== menu cadastros ===")
    print("1 - adicionar nome")
    print("2 - cadastrar sobrenomes" )
    print("3 - consultar cadastros")
    print("4 - excluir cadastros")
    print("5 - sair do sistema"  )

    opcao = input("Escolha sua opcao: ")
    
 
    if opcao == "1":
        nome = input("Digite seu nome: ")
        nomes.append(nome)
        print("nome adicionado com sucesso!")


    if opcao == "2":
        nome = input("Digite seu sobrenome: ")
        nomes.append(nome)
        print("sobrenome adicionado com sucesso!")


    elif opcao == "3":
        if len(nomes) == 0:
           print("encontrado")
        else:
            for nome in nomes:
                print(nome)


    elif opcao == "4":
        if len(nomes) == 0:
            print("não existem nomes cadastrados")
        else:
            for index, name in enumerate(nomes):
                print(f"{index + 1}. {nome}")
            opcao = int(input("digite a opção que voce quer deletar..."))
            nomes.remove(nomes[opcao - 1])
            print("valor removido com sucesso")

  

    elif opcao == "5":
        print("saindo do sistema")
        break
    else:
        print("opção inexistente, tente novamente...")
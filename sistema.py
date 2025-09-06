# sistema de tarefas 
tarefas = [] # lista vazia 

while True:
    print("=== menu tarefas ===")
    print("1 - adicionar tarefa")
    print("2 - listar tarefas"  )
    print("3- sair do sistema"  )

    opcao = input("Escolha sua opcao: ")
    
 #adcionar tarefas 
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        #append -> adicionar a lista
        tarefas.append(tarefa)
        print("tarefa adicionada com sucesso!")

# Listar tarefas
    elif opcao == "2":
        # len -> length -> tamanho
        if len(tarefas) == 0:
           print("não existem tarefas cadastradas")
        else:
            for tarefa in tarefas:
                print(tarefa)

    elif opcao == "9":
        print("saindo do sistema")
        break
    else:
        print("opção inexistente, tente novamente...")
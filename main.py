def tarefas():
    #guarda tarefas
    tarefas_salvas = []
    # Função para adicionar e listar tarefa
    while True:
        print("=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. remover tarefa")
        print("0. Sair")
        interacao = input("Escolha uma opção: ")
        

        if interacao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas_salvas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada com sucesso!")

        elif interacao == "2":
            if len(tarefas_salvas) == 0:
                print("Nenhuma tarefa salva")

            else:       
                print("Listando tarefas...")
                for numero, tarefa in enumerate (tarefas_salvas, start = 1):
                    print(f"{numero} - {tarefa}")

        elif interacao == "3":
            for numero, tarefa in enumerate (tarefas_salvas, start = 1):
                print(f"{numero} - {tarefa}")
            remover = input("escolha a opcão que deseja remover")
            remover = int(remover)
            tarefas_salvas.pop(remover - 1)
            
            


        elif interacao == "0":
            print("Saindo do gerenciador de tarefas.")
            break

tarefas()

tarefas = []

while True:
    print("\n=== TASK MANAGER v1.0 ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # Validar entrada
    if opcao not in ["1", "2", "3"]:
        print("❌ Opção inválida! Digite 1, 2 ou 3")
        continue

    # Processar opção
    if opcao == "1":
        # Subfunção: criar tarefa
        nome = input("Nome da tarefa: ")
        if nome.strip():  # Validar que não está vazio
            tarefas.append(nome)
            print(f"✅ Tarefa '{nome}' criada com sucesso!")
        else:
            print("❌ Nome da tarefa não pode ser vazio!")

    elif opcao == "2":
        # Subfunção: listar tarefas
        if len(tarefas) == 0:
            print("📪 Nenhuma tarefa registrada ainda")
        else:
            print("\n📋 Suas tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"  {i}. {tarefa}")

    elif opcao == "3":
        # Subfunção: sair
        print("👋 Até logo!")
        break
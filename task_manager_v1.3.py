opcao = input("Opção: ")

if opcao == "1":
    while True: # Loop aninhado
        print("\n=== Tarefas ===")
        for i, (tarefa, completa) in enumerate(zip(tarefas, completas), 1):
            status = "✅" if completa else "⏳"
            print(f"{i}. {status} {tarefa}")

        sub_opcao = input("\nEscolha tarefa (número) ou '0' para voltar: ")

        if sub_opcao == "0"
            break # Sai do loop aninhado

        if sub_opcao.isdigit():
            idx = int(sub_opcao) - 1
            if 0 <= idx < len(tarefas):
                print(f"\nOpções: 1-Marcar completa 2-Deletar 3-Voltar")
                acao = input("Ação: ")

            if acao =="1":
                completas[idx] = True
                print("✅ Marcada como completa!")
            elif acao == "2":
                tarefas.pop(idx)
                completas.pop(idx)
                print("✅ Tarefa deletada!")
            # acao == "3" ou outra: continue volta ao submenu
            else:
                print("❌ Inválido")
            else:
            print("❌ Digite um número")

        elif opcao == "2":
            print("👋 Até logo!")
            break # Sai do loop principal
        else:
            print("❌ Opção inválida")
            continue # Volta ao ínicio do loop


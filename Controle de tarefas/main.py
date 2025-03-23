import tarefas

# Função principal que exibe o menu
def menu():
    lista_tarefas = []
    
    while True:
        print("\n----- Sistema de Gerenciamento de Tarefas -----")
        print(50*'-')
        print("1. Adicionar nova tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Listar todas as tarefas")
        print("4. Sair")
        print(50*'-')
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print(50*'-')
            titulo = input("Digite o título da tarefa: ").capitalize()
            descricao = input("Digite a descrição da tarefa: ").capitalize()
            tarefas.adicionar_tarefa(lista_tarefas, titulo, descricao)
        
        elif opcao == "2":
            print(50*'-')
            titulo = input("Digite o título da tarefa a ser concluída: ").capitalize()
            tarefas.concluir_tarefa(lista_tarefas, titulo)
        
        elif opcao == "3":
            print(50*'-')
            tarefas.listar_tarefas(lista_tarefas)
        
        elif opcao == "4":
            print(50*'-')
            print("Saindo do programa...")
            break
        
        else:
            print(50*'-')
            print("Opção inválida! Tente novamente.")

menu()
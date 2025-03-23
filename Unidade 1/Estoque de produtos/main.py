import estoque

# Função que exibe o menu
def menu():
    estoque_atual = {} 

    while True:
        print("\n----- Sistema de Gerenciamento de Estoque -----")
        print(50*'-')
        print("1. Adicionar produto ao estoque")
        print("2. Remover produto do estoque")
        print("3. Atualizar quantidade de produto")
        print("4. Exibir todos os produtos no estoque")
        print("5. Sair")
        print(50*'-')
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(50*'-')
            nome = input("Digite o nome do produto: ").capitalize()
            quantidade = int(input("Digite a quantidade do produto: "))
            estoque.adicionar_produto(estoque_atual, nome, quantidade)
        elif opcao == "2":
            print(50*'-')
            nome = input("Digite o nome do produto a ser removido: ").capitalize()
            estoque.remover_produto(estoque_atual, nome)
        elif opcao == "3":
            print(50*'-')
            nome = input("Digite o nome do produto para atualizar a quantidade: ").capitalize()
            quantidade = int(input("Digite a nova quantidade: "))
            estoque.atualizar_quantidade(estoque_atual, nome, quantidade)
        elif opcao == "4":
            print(50*'-')
            estoque.exibir_estoque(estoque_atual)
        elif opcao == "5":
            print(50*'-')
            print("Saindo do programa...")
            break
        else:
            print(50*'-')
            print("Opção inválida! Tente novamente.")

menu()

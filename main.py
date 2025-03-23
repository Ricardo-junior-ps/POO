import alunos

# Função principal que exibe o menu e realiza as operações de cadastro de alunos
def menu():
    alunos_cadastrados = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }

    while True:
        print("\n----- Sistema de Cadastro de Alunos -----")
        print(50*"-")
        print("1. Adicionar aluno")
        print("2. Atualizar notas de um aluno")
        print("3. Remover aluno")
        print("4. Exibir todos os alunos e suas notas")
        print("5. Sair")
        print(50*"-")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(50*"-")
            nome = input("Digite o nome do aluno: ").capitalize()
            notas = []
            for i in range(1, 5):
                nota = float(input(f"Digite a nota {i} do aluno: "))
                notas.append(nota)
            alunos.adicionar_aluno(alunos_cadastrados, nome, notas)
        elif opcao == "2":
            print(50*"-")
            nome = input("Digite o nome do aluno para atualizar as notas: ").capitalize()
            novas_notas = []
            for i in range(1, 5):
                nota = float(input(f"Digite a nova nota {i} do aluno: "))
                novas_notas.append(nota)
            alunos.atualizar_notas(alunos_cadastrados, nome, novas_notas)
        elif opcao == "3":
            print(50*"-")
            nome = input("Digite o nome do aluno a ser removido: ").capitalize()
            alunos.remover_aluno(alunos_cadastrados, nome)
        elif opcao == "4":
            print(50*"-")
            alunos.exibir_alunos(alunos_cadastrados)
        elif opcao == "5":
            print(50*"-")
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()

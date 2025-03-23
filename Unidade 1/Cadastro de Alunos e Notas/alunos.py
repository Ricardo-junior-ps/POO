# Função para adicionar um aluno e suas notas
def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print(f"O aluno '{nome}' já está cadastrado. Tente atualizar as notas.")
    else:
        alunos[nome] = notas
        print(f"Aluno '{nome}' adicionado com sucesso!")

# Função para atualizar as notas de um aluno
def atualizar_notas(alunos, nome, novas_notas):
    if nome in alunos:
        alunos[nome] = novas_notas
        print(f"As notas do aluno '{nome}' foram atualizadas com sucesso.")
    else:
        print(f"O aluno '{nome}' não está cadastrado.")

# Função para remover um aluno do cadastro
def remover_aluno(alunos, nome):
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno '{nome}' removido do cadastro com sucesso.")
    else:
        print(f"O aluno '{nome}' não está cadastrado.")

# Função para exibir todos os alunos e suas notas
def exibir_alunos(alunos):
    if alunos:
        print("\nAlunos e suas notas:")
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f"{nome}: {notas} - Média = {media}")
    else:
        print("\nNão há alunos cadastrados.")


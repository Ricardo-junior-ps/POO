from persistencia import carregar_alunos, carregar_professores, carregar_disciplinas

if __name__ == "__main__":

    alunos = carregar_alunos()
    professores = carregar_professores() 
    disciplinas = carregar_disciplinas(professores, alunos) 

    print("\n--- Alunos ---") # Exibe os dados de cada aluno
    for aluno in alunos:
        print(aluno.exibir_dados(), "\n")

    print("\n--- Professores ---") # Exibe os dados de cada professor
    for prof in professores:
        print(prof.exibir_dados(), "\n")

    print("\n--- Disciplinas ---") # Exibe os dados de cada disciplina
    for disc in disciplinas:
        print(disc.exibir_dados(), "\n")

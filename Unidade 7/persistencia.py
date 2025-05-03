import os
from classes import *

def ler_alunos(nome_arquivo): # Função para ler os dados de alunos a partir do arquivo de texto alunos.txt
    alunos = {}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|') # Divide os dados pelo caractere '|'
                nome = dados[0].strip()
                cpf = dados[1].strip()
                data_nascimento = dados[2].strip()
                codigo = dados[3].strip()

                # Cria uma instância de Aluno
                aluno = Aluno(nome, cpf, data_nascimento, codigo)
                for i in range(4, len(dados)): 
                    disciplina_notas = dados[i].strip().split(',')
                    nome_disciplina = disciplina_notas[0].strip()
                    notas = [float(nota.strip()) for nota in disciplina_notas[1:]]
                    aluno.adicionar_disciplina(nome_disciplina, notas)

                alunos[codigo] = aluno  # Armazena o aluno no dicionário
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    return alunos

def ler_professores(nome_arquivo): # Função para ler os dados de alunos a partir do arquivo de texto professores.txt
    professores = {}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                codigo = dados[0].strip()
                nome = dados[1].strip()
                cpf = dados[2].strip()
                data_nascimento = dados[3].strip()

                # Cria uma instância de Professor
                professor = Professor(nome, cpf, data_nascimento, codigo)

                for disciplina in dados[4:]:  # Adiciona todas as disciplinas que o professor ministra
                    professor.adicionar_disciplina(disciplina.strip())
                professores[codigo] = professor
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    return professores

def ler_disciplinas(nome_arquivo, professores, alunos): # Função para ler os dados de alunos a partir do arquivo de texto disciplinas.txt e relacionar com professores e alunos
    disciplinas = {}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                codigo = dados[0].strip()
                nome_disciplina = dados[1].strip()
                nome_professor = dados[2].strip()

                professor = None  # Procura o professor pelo nome
                for prof in professores.values():
                    if prof.nome == nome_professor:
                        professor = prof
                        break

                if professor: # Cria a disciplina associada ao professor encontrado
                    disciplina = Disciplina(codigo, nome_disciplina, professor)

                    # Adiciona os alunos listados na disciplina 
                    alunos_disciplina = [aluno_nome.strip() for aluno_nome in dados[3].split(',')]
                    for aluno_nome in alunos_disciplina:
                        for aluno in alunos.values():
                            if aluno.nome == aluno_nome:
                                disciplina.adicionar_aluno(aluno)
                                break

                    # Armazena a disciplina no dicionário
                    disciplinas[codigo] = disciplina
                else:
                    print(f"Aviso: Professor '{nome_professor}' não encontrado para a disciplina '{nome_disciplina}'.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    return disciplinas

# Caminho da pasta dos arquivos
pasta_arquivos = r"C:\Users\ricar\OneDrive\Área de Trabalho\IFCE - Técnico em Informática para Internet\Atividades\POO\Unidade 7"

# Leitura dos arquivos
alunos = ler_alunos(os.path.join(pasta_arquivos, "alunos.txt"))
professores = ler_professores(os.path.join(pasta_arquivos, "professores.txt"))
disciplinas = ler_disciplinas(os.path.join(pasta_arquivos, "disciplinas.txt"), professores, alunos)

# Exibição dos dados das instâncias
print("\n--- Dados dos Alunos ---")
for aluno in alunos.values():
    print(aluno.exibir_dados())

print("\n--- Dados dos Professores ---")
for professor in professores.values():
    print(professor.exibir_dados())

print("\n--- Dados das Disciplinas ---")
for disciplina in disciplinas.values():
    print(disciplina.exibir_dados())
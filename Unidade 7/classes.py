class Pessoa: # Classe Pessoa, representa uma pessoa com nome, CPF e data de nascimento
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def exibir_dados(self): # Método para retornar uma string com os dados da pessoa
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"

class Aluno(Pessoa): # Classe Aluno herda de Pessoa e adiciona um código e disciplinas com notas
    def __init__(self, nome, cpf, data_nascimento, codigo):
        super().__init__(nome, cpf, data_nascimento)
        self.codigo = codigo
        self.disciplinas = {} # Dicionário para armazenar disciplinas e notas

    def adicionar_disciplina(self, disciplina, notas):  # Método para adicionar uma disciplina e suas notas ao aluno
        self.disciplinas[disciplina] = notas

    def exibir_dados(self): # Método para exibir todos os dados do aluno, incluindo as notas por disciplina
        dados_aluno = f"{super().exibir_dados()}, Código: {self.codigo}"
        for disciplina, notas in self.disciplinas.items():
            dados_aluno += f"\n  {disciplina}: {', '.join(map(str, notas))}"
        return dados_aluno

class Professor(Pessoa): # Classe Professor herda de Pessoa e adiciona um código e lista de disciplinas que leciona
    def __init__(self, nome, cpf, data_nascimento, codigo):
        super().__init__(nome, cpf, data_nascimento)
        self.codigo = codigo
        self.disciplinas = [] # Lista de nomes de disciplinas que o professor ministra

    def adicionar_disciplina(self, disciplina): # Adiciona uma disciplina à lista do professor
        self.disciplinas.append(disciplina)

    def exibir_dados(self): # Exibe os dados do professor, incluindo as disciplinas que leciona
        return f"{super().exibir_dados()}, Código: {self.codigo}, Disciplinas: {', '.join(self.disciplinas)}"

class Disciplina: # Classe Disciplina representa uma disciplina com código, nome, professor responsável e lista de alunos
    def __init__(self, codigo, nome, professor):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno): # Adiciona um aluno à disciplina
        self.alunos.append(aluno)

    def exibir_dados(self): # Exibe os dados da disciplina, incluindo nome do professor e nomes dos alunos
        return f"Código: {self.codigo}, Disciplina: {self.nome}, Professor: {self.professor}, Alunos: {', '.join([aluno.nome for aluno in self.alunos])}"
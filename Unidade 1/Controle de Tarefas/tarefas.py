# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, titulo, descricao):
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'status': 'Pendente'
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(tarefas, titulo):
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo:
            tarefa['status'] = 'Concluído'
            print(f"Tarefa '{titulo}' marcada como concluída!")
            return
    print(f"Tarefa '{titulo}' não encontrada.")

# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    pendentes = [t for t in tarefas if t['status'] == 'Pendente']
    concluídas = [t for t in tarefas if t['status'] == 'Concluído']
    
    print("\nTarefas Pendentes:")
    if pendentes:
        for t in pendentes:
            print(f"- {t['titulo']}: {t['descricao']}")
    else:
        print("Nenhuma tarefa pendente.")
    
    print("\nTarefas Concluídas:")
    if concluídas:
        for t in concluídas:
            print(f"- {t['titulo']}: {t['descricao']}")
    else:
        print("Nenhuma tarefa concluída.")

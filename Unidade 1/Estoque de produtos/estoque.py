# Função para adicionar um novo produto ao estoque
def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print(f"{nome} já está no estoque. Tente atualizar a quantidade.")
    else:
        estoque[nome] = quantidade
        print(f"{quantidade} unidade(s) de {nome} adicionado ao estoque.")

# Função para remover um produto do estoque
def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print(f"{nome} removido do estoque.")
    else:
        print(f"{nome} não encontrado no estoque.")

# Função para atualizar a quantidade de um produto existente
def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"A quantidade de '{nome}' foi atualizada para {quantidade} unidades.")
    else:
        print(f"{nome} não encontrado no estoque.")

# Função para exibir todos os produtos no estoque
def exibir_estoque(estoque):
    if estoque:
        print("\nEstoque atual:")
        for nome, quantidade in estoque.items():
            print(f"Produto: {nome} - Quantidade: {quantidade} unidades")
    else:
        print("\nO estoque está vazio.")

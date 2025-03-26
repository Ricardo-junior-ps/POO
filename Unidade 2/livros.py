class livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

    def informacoes(self):
        print(80*"-")
        print(f"Título: {self.titulo} -- Autor: {self.autor} -- Ano: {self.ano_publicacao} -- Preço: R$ {self.preco}")
        print(80*"-")

livro1 = livro("O Quinze", "Raquel de Queiroz", 1930, 37.80)
livro2 = livro("Dom Casmurro" , "Machado de Assis", 1899, 10.66)

livro1.informacoes()
livro2.informacoes()
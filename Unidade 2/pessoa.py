class pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentacao(self):
        print(56*"-")
        print(f"Olá, meu nome é {self.nome}, tehho {self.idade} anos e moto em {self.cidade}")
        print(56*"-")

pessoa1 = pessoa("João", "22", "São Paulo")

pessoa1.apresentacao()
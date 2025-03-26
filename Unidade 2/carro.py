class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca  # Atributo: marca do carro
        self.modelo = modelo  # Atributo: modelo do carro
        self.ano = ano  # Atributo: ano de fabricação
        self.cor = cor  # Atributo: cor do carro
    
    def informacoes(self):
        # Método para exibir as informações do carro
        print(30*"-")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(30*"-")

# Criando um objeto da classe Carro
carro1 = Carro("Onix", "Chevrolet ", 2025, "Prata")

# Exibindo as informações do carro
carro1.informacoes()

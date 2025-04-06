class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        # Construtor com passagem de parâmetros
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        # Método que exibe as informações do restaurante
        print(f"Restaurante: {self.nomeRestaurante} ---- Tipo de Cozinha: {self.tipoCozinha}")

    def abrirRestaurante(self):
        # Método que exibe mensagem de restaurante aberto
        print(f"{self.nomeRestaurante} está aberto!")

    def __str__(self):
        # Método __str__ para representar o objeto de maneira legível
        print(f"Restaurante: {self.nomeRestaurante} - Tipo de Cozinha: {self.tipoCozinha}")


# Criando três objetos Restaurante
restaurante1 = Restaurante("Pizza Hut", "Italiana")
restaurante2 = Restaurante("JapaMania", "Japonesa")
restaurante3 = Restaurante("Burguer King", "Fast Food")

# Chamando o método __str__ para cada um dos objetos
restaurante1.__str__()
restaurante1.abrirRestaurante()
print(50*"-")
restaurante2.__str__()
restaurante2.abrirRestaurante()
print(50*"-")
restaurante3.__str__()
restaurante3.abrirRestaurante()
print(50*"-")
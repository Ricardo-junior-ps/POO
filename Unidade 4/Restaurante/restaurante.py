class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = 0  # Valor padrão

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante} ---- Tipo de Cozinha: {self.tipoCozinha}")

    def abrirRestaurante(self):
        print(f"{self.nomeRestaurante} está aberto!")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} - Tipo de Cozinha: {self.tipoCozinha}"

    def getNumeroServidos(self):
        return self.numeroServidos

    def setNumeroServidos(self, numero):
        if numero >= 0:
            self.numeroServidos = numero
        else:
            print("Número inválido de clientes servidos.")

    def incrementeNumeroServidos(self, incremento):
        if incremento > 0:
            novo_valor = self.getNumeroServidos() + incremento
            self.setNumeroServidos(novo_valor)
        else:
            print("Incremento inválido.")

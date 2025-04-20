from abc import ABC, abstractmethod

# Classe abstrata
class CartaoWeb(ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass

# Classe filha para Dia dos Namorados
class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}! Que o amor esteja sempre presente em nossas vidas.")

# Classe filha para Natal
class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}! Que seu dia seja cheio de paz, amor e alegria.")

# Classe filha para Aniversário
class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}! Que seu novo ano seja repleto de conquistas e felicidades.")



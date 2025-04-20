from abc import ABC, abstractmethod

# Classe abstrata
class MetodoPagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass

# Classe concreta: Cartão de Crédito
class CartaoCredito(MetodoPagamento):
    def pagar(self):
        taxa = self.valor * 0.05
        total = self.valor + taxa
        print(f"Pagamento com Cartão de Crédito")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Taxa de 5%: R$ {taxa:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

# Classe concreta: Boleto Bancário
class BoletoBancario(MetodoPagamento):
    def pagar(self):
        desconto = self.valor * 0.02
        total = self.valor - desconto
        print(f"Pagamento com Boleto Bancário")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Desconto de 2%: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

# Classe concreta: Pix
class Pix(MetodoPagamento):
    def pagar(self):
        print(f"Pagamento com Pix")
        print(f"Valor original e total: R$ {self.valor:.2f} (sem descontos ou taxas)")


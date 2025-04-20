from Pagamento import *

# Programa principal
if __name__ == "__main__":
    print("=== Sistema de Pagamento ===")
    valor = float(input("Informe o valor da compra: R$ "))
    print("Escolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto Bancário")
    print("3 - Pix")

    escolha = input("Opção: ")

    pagamento: MetodoPagamento  # Referência do tipo abstrato

    if escolha == "1":
        pagamento = CartaoCredito(valor)
    elif escolha == "2":
        pagamento = BoletoBancario(valor)
    elif escolha == "3":
        pagamento = Pix(valor)
    else:
        print("Opção inválida.")
        exit()

    pagamento.pagar()


# O polimorfismo permite usar uma única referência para diferentes formas de pagamento, simplificando o código.
# A interface abstrata garante que todas as classes implementem  o método pagar(), tornando o sistema mais flexível, 
# organizado e fácil de manter.

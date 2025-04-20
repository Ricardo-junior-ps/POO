from cartoes import *


if __name__ == "__main__":
    # variável de referência do tipo CartaoWeb
    cartao: CartaoWeb

    # Atribuindo uma instância de DiaDosNamorados
    cartao = DiaDosNamorados("Maria")
    cartao.showMessage()

    # Atribuindo uma instância de Natal
    cartao = Natal("João")
    cartao.showMessage()

    # Atribuindo uma instância de Aniversario
    cartao = Aniversario("Ana")
    cartao.showMessage()


# Questão:
# O polimorfismo acontece quando a variável cartao, do tipo CartaoWeb, é usada para chamar o método showMessage de diferentes subclasses.
# Mesmo sendo a mesma variável, o comportamento muda conforme a instância.
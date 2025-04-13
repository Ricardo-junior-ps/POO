from agencia import Usuario, ContaPoupanca, ContaCorrente, ContaEspecial
from datetime import datetime
import random

def main():
    print("-" * 80)
    nome = input("Digite o nome do usuário: ").capitalize()
    print("-" * 80)
    cpf = int(input("Digite o CPF do usuário: "))
    print("-" * 80)
    rg = int(input("Digite o RG do usuário: "))
    print("-" * 80)
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    print("-" * 80)
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    usuario = Usuario(nome=nome, cpf=cpf, rg=rg, dataNascimento=data_nascimento)
    data_abertura = datetime.now()

    # Criando uma conta de cada tipo
    cp = ContaPoupanca(random.randint(0, 999), usuario, data_abertura, saldo=1000)
    cc = ContaCorrente(random.randint(0, 999), usuario, data_abertura, saldo=500)
    ce = ContaEspecial(random.randint(0, 999), usuario, data_abertura, saldo=100, limite=1000)

    print("\n--- Conta Poupança ---")
    cp.consultarSaldo()
    cp.aplicarRendimento()
    cp.consultarSaldo()

    print("\n--- Conta Corrente ---")
    cc.consultarSaldo()
    cc.descontarTaxa()
    cc.consultarSaldo()

    print("\n--- Conta Especial ---")
    ce.consultarSaldo()
    ce.sacar(900)  # Dentro do limite
    ce.consultarSaldo()
    ce.transferir(cp, 150)  # Usando cheque especial
    ce.consultarSaldo()
    cp.consultarSaldo()

if __name__ == "__main__":
    main()

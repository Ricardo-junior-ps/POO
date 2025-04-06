from agencia import Usuario, Conta
from datetime import datetime
import random

def main():
    #Instanciando objeto Usuario com valores padrão
    usuario = Usuario()

    #entrada de valores
    print(80*'-')
    nome = input("Digite o nome do usuário: ").capitalize()
    print(80*'-')
    cpf = int(input("Digite o CPF do usuário: "))
    print(80*'-')
    rg = int(input("Digite o RG do usuário: "))
    print(80*'-')
    data_nascimento = input("Digite a data de nascimento do usuário (formato: dd/mm/aaaa): ")
    print(80*'-')
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    #Atribuir valores aos atributos do usuário
    usuario.definir_rg(rg)
    usuario.definir_cpf(cpf)
    usuario.definir_nome(nome)
    usuario.definir_dataNascimento(data_nascimento)

    #Gerar o código da agência aleatoriamente entre 0 e 999
    agencia = random.randint(0, 999)

    #Instanciando o objeto Conta
    data_abertura = datetime.now()
    conta = Conta(agencia, usuario, data_abertura)

    #Exibe os dados da conta e do usuário
    print("\nDados da Conta")
    print(f"Agência: {conta.obter_agencia()}")
    print(f"Data de Abertura: {conta.obter_dataAbertura().strftime('%d/%m/%Y')}")
    print(f"Saldo: R${conta.obter_saldo():.2f}")

    print("\nDados do Usuário")
    print(f"Nome: {conta.obter_usuario().obter_nome()}")
    print(f"RG: {conta.obter_usuario().obter_cpf()}")
    print(f"CPF: {conta.obter_usuario().obter_cpf()}")
    print(f"Data de Nascimento: {conta.obter_usuario().obter_dataNascimento().strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    main()

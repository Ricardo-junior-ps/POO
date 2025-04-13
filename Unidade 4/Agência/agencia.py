import random
from datetime import datetime

# Classe Usuario
class Usuario:
    def __init__(self, rg=None, cpf=None, nome=None, dataNascimento=None):
        self.rg = rg if rg is not None else 0
        self.cpf = cpf if cpf is not None else 0
        self.nome = nome if nome is not None else "Não Informado"
        self.dataNascimento = dataNascimento if dataNascimento is not None else datetime(1900, 1, 1)

    def definir_rg(self, rg): self.rg = rg
    def definir_cpf(self, cpf): self.cpf = cpf
    def definir_nome(self, nome): self.nome = nome
    def definir_dataNascimento(self, dataNascimento): self.dataNascimento = dataNascimento

    def obter_rg(self): return self.rg
    def obter_cpf(self): return self.cpf
    def obter_nome(self): return self.nome
    def obter_dataNascimento(self): return self.dataNascimento

# Classe Conta
class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo=0.0):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def definir_agencia(self, agencia): self.agencia = agencia
    def definir_usuario(self, usuario): self.usuario = usuario
    def definir_dataAbertura(self, dataAbertura): self.dataAbertura = dataAbertura
    def definir_saldo(self, saldo): self.saldo = saldo

    def obter_agencia(self): return self.agencia
    def obter_usuario(self): return self.usuario
    def obter_dataAbertura(self): return self.dataAbertura
    def obter_saldo(self): return self.saldo

    def consultarSaldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, destino, valor):
        if isinstance(destino, Conta) and valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        else:
            print("Transferência não realizada. Verifique saldo ou conta de destino.")

# Conta Poupança
class ContaPoupanca(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0.0, rendimentoMensal=0.005):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.rendimentoMensal = rendimentoMensal

    def aplicarRendimento(self):
        rendimento = self.saldo * self.rendimentoMensal
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado.")

# Conta Corrente
class ContaCorrente(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0.0, taxaManutencao=10.0):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.taxaManutencao = taxaManutencao

    def descontarTaxa(self):
        if self.saldo >= self.taxaManutencao:
            self.saldo -= self.taxaManutencao
            print(f"Taxa de manutenção de R${self.taxaManutencao:.2f} descontada.")
        else:
            print("Saldo insuficiente para descontar taxa.")

# Conta Especial
class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0.0, limite=500.0):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.limite = limite

    def consultarSaldo(self):
        saldo_total = self.saldo + self.limite
        print(f"Saldo disponível (incluindo limite): R${saldo_total:.2f}")
        return saldo_total

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Limite de saque excedido.")

    def transferir(self, destino, valor):
        if isinstance(destino, Conta) and valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        else:
            print("Transferência não realizada. Verifique limite ou conta de destino.")

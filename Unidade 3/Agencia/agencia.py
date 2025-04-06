import random
from datetime import datetime

# Classe Usuario
class Usuario:
    def __init__(self, rg=None, cpf=None, nome=None, dataNascimento=None):
        self.rg = rg if rg is not None else 0
        self.cpf = cpf if cpf is not None else 0
        self.nome = nome if nome is not None else "Não Informado"
        self.dataNascimento = dataNascimento if dataNascimento is not None else datetime(1900, 1, 1)

    # Métodos modificadores (set)
    def definir_rg(self, rg):
        self.rg = rg

    def definir_cpf(self, cpf):
        self.cpf = cpf

    def definir_nome(self, nome):
        self.nome = nome

    def definir_dataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    # Métodos de acesso (get)
    def obter_rg(self):
        return self.rg

    def obter_cpf(self):
        return self.cpf

    def obter_nome(self):
        return self.nome

    def obter_dataNascimento(self):
        return self.dataNascimento


# Classe Conta
class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo=0.0):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    # Métodos modificadores (set)
    def definir_agencia(self, agencia):
        self.agencia = agencia

    def definir_usuario(self, usuario):
        self.usuario = usuario

    def definir_dataAbertura(self, dataAbertura):
        self.dataAbertura = dataAbertura

    def definir_saldo(self, saldo):
        self.saldo = saldo

    # Métodos de acesso (get)
    def obter_agencia(self):
        return self.agencia

    def obter_usuario(self):
        return self.usuario

    def obter_dataAbertura(self):
        return self.dataAbertura

    def obter_saldo(self):
        return self.saldo

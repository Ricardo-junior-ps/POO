class Veiculo:
    total_veiculos = 0  # Atributo de classe

    def __init__(self, placa, modelo, diaria):
        self.__placa = placa  # privado
        self.modelo = modelo  # público
        self.diaria = diaria  # público
        self.__alugado = False  # privado
        Veiculo.total_veiculos += 1

    # Propriedade para a placa (somente leitura)
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        print("Erro: A placa do veículo não pode ser modificada!")

    # Métodos de instância
    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"O veículo {self.modelo} foi alugado com sucesso.")
        else:
            print(f"O veículo {self.modelo} já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"O veículo {self.modelo} foi devolvido com sucesso.")
        else:
            print(f"O veículo {self.modelo} já está disponível.")

    def status(self):
        estado = "Alugado" if self.__alugado else "Disponível"
        print(f"Status do veículo {self.modelo} ({self.__placa}): {estado}")

    # Método de classe
    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")
        
    # Método estático
    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        return dias * diaria
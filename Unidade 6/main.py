from locadora import *

# Criando veículos
veiculo1 = Veiculo("ABC-1234", "Fiat Uno", 100.0)
veiculo2 = Veiculo("XYZ-5678", "Toyota Corolla", 200.0)

# Alugar um veículo e exibir status
veiculo1.alugar()
veiculo1.status()

# Devolver o veículo e exibir status
veiculo1.devolver()
veiculo1.status()

# Exibir a placa e tentar modificar
print(f"Placa do veículo: {veiculo1.placa}")
veiculo1.placa = "NOV-9999"  # Tentativa de alteração

# Mostrar total de veículos
Veiculo.mostrar_total_veiculos()

# Calcular e exibir valor do aluguel
dias_alugados = 5
preco_total = Veiculo.calcular_preco_aluguel(dias_alugados, veiculo2.diaria)
print(f"Valor do aluguel do {veiculo2.modelo} por {dias_alugados} dias: R${preco_total:.2f}")
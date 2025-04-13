from restaurante import Restaurante

def main():
    # Criando instância
    restaurante1 = Restaurante("Pizza Hut", "Italiana")
    restaurante2 = Restaurante("JapaMania", "Japonesa")
    restaurante3 = Restaurante("Burguer King", "Fast Food")

    print("\n--- Informações do Restaurante ---")
    print(restaurante1)
    restaurante1.abrirRestaurante()

    # 1. Mostrar número de clientes servidos e alterar o valor
    print(f"\nNúmero de clientes servidos inicialmente: {restaurante1.getNumeroServidos()}")
    restaurante1.setNumeroServidos(45)
    print(f"Número de clientes servidos após alteração: {restaurante1.getNumeroServidos()}")

    # 2. Alterar valor novamente com set e mostrar com get
    restaurante1.setNumeroServidos(120)
    print(f"Número de clientes servidos após nova alteração: {restaurante1.getNumeroServidos()}")

    # 3. Incrementar número de clientes
    restaurante1.incrementeNumeroServidos(30)
    print(f"Número de clientes servidos após incremento: {restaurante1.getNumeroServidos()}")

    #---------------------------------------------------------------------------------------

    print("\n--- Informações do Restaurante ---")
    print(restaurante2)
    restaurante2.abrirRestaurante()

    print(f"\nNúmero de clientes servidos inicialmente: {restaurante2.getNumeroServidos()}")
    restaurante2.setNumeroServidos(15)
    print(f"Número de clientes servidos após alteração: {restaurante2.getNumeroServidos()}")

    restaurante2.setNumeroServidos(50)
    print(f"Número de clientes servidos após nova alteração: {restaurante2.getNumeroServidos()}")

    restaurante2.incrementeNumeroServidos(20)
    print(f"Número de clientes servidos após incremento: {restaurante2.getNumeroServidos()}")

    #---------------------------------------------------------------------------------------

    print("\n--- Informações do Restaurante ---")
    print(restaurante3)
    restaurante3.abrirRestaurante()

    print(f"\nNúmero de clientes servidos inicialmente: {restaurante3.getNumeroServidos()}")
    restaurante3.setNumeroServidos(20)
    print(f"Número de clientes servidos após alteração: {restaurante3.getNumeroServidos()}")

    restaurante3.setNumeroServidos(40)
    print(f"Número de clientes servidos após nova alteração: {restaurante3.getNumeroServidos()}")

    restaurante3.incrementeNumeroServidos(40)
    print(f"Número de clientes servidos após incremento: {restaurante3.getNumeroServidos()}")


if __name__ == "__main__":
    main()

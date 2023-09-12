class Automovel:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")

# Criando objetos para representar carros de locadoras
locadora1 = Automovel("Toyota", 2022)
locadora2 = Automovel("Ford", 2023)
locadora3 = Automovel("Honda", 2021)

# Imprimindo as informações dos carros
print("Carro da Locadora 1:")
locadora1.exibir_informacoes()

print("\nCarro da Locadora 2:")
locadora2.exibir_informacoes()

print("\nCarro da Locadora 3:")
locadora3.exibir_informacoes()

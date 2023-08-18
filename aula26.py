def calcular_potencia(base, expoente=2):
    resultado = base ** expoente
    return resultado

# Exemplos de uso da função
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente (opcional, pressione Enter para usar o padrão): ") or 2)

resultado = calcular_potencia(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é {resultado}.")

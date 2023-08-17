def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

# Solicitar um número do usuário
numero_digitado = float(input("Digite um número: "))

# Chamar a função e imprimir o resultado
resultado = calcular_quadrado(numero_digitado)
print(f"O quadrado de {numero_digitado} é {resultado}.")

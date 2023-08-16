# Criando a lista de frutas
frutas = ["maçã", "banana", "abacate", "tangerina", "limão", "maçã", "maçã", "none"]

# Inicializando a variável de contagem
contagem_macas = 0

# Usando um loop for para contar quantas vezes "maçã" aparece na lista
for fruta in frutas:
    if fruta == "maçã":
        contagem_macas += 1

# Imprimindo o resultado
print("A palavra 'maçã' aparece", contagem_macas, "vezes na lista de frutas.")

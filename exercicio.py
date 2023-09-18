"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        Aprimeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios

"""
nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))

if nome and idade:
    print(f"Seu nome e sua idade são: {nome} , {idade}.")
    print(f"Seu nome invertido é: {nome[::-1]}")

    if " " in nome:
        print(f"Seu nome {nome}, contém espaços.")

    else:
        print(f"Seu nome {nome}, não contém espaços.")

    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")


else:
    print("Desculpe, você deixou campos vazios")

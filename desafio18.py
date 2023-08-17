#lista de carros em estoque
carros_em_estoque['BMW X6', 'BMW i5', 'BMW i8' ]

#Solicitar ao usuário o nome do carro desejado
carro_desejado = input('Digite o nome do carro que deseja comprar: ')

#Verificar se o carro está em estoque
if carro_desejado in carro_em_estoque:
    print('Este carro está disponível.')

else:
    print('Não temos esse carro disponível.')
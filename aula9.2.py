'''
Operadores relacionais (de comparação) em Python
Operadores de comparação (relacionais)
Op      significado        exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente            'a' != 'b'
'''
'''
maior = 2 > 1
maior_igual = 2 >= 2
menor = 1 < 2
menor_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)
'''
#Exercício de programação com if e comparação

'''
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo.')
elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior.')

else:
    print('Nenhuma das opções')
'''
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:
    print(
    f'{primeiro_valor=} é maior ou igual' 
    f' ao {segundo_valor}'
    )

else:
    print(
          f'{segundo_valor=} é maior '  
          f'do que {primeiro_valor=}'
          )



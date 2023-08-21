'''
#introdução aos blocos de códigos
#if  / elif       /else
#se / se não se / se não
entrada = input('vc quer entrar ou sair? ')

if entrada == 'entrar':
    print('vc entrou no sistema.')
elif entrada == 'sair':
    print('vc saiu do sistema.')

else:
    print('Vc n digitou nem entrar, nem sair.')

print('Fora dos blocos')
'''
#if, elif e else: entendendo o fluxo do interpretador em condicionais
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True


if condicao1:
    print('Este é o código do if. ')
elif condicao2:
    print('Código da condição 2.')
elif condicao3:
    print('Condição 3.')
elif condicao4:
    print('Condição 4.')
else: 
    print('Nenhuma condição é verdadeira.')

if 10 == 10:
    print('Outro if.')

#O Debugger do VS Code e o interpretador do Python lendo os códigos
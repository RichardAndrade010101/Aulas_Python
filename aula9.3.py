#operadores lógicos
#and (e) or (ou) not (não)
#and - todas as condições precisam ser verdadeiras 
#se qualquer valor for considerado falso,
#a expressão inteira será avaliada naquele valor
#são considerados falsy 
#0.0.0.0 '' False
#Também existe o tipo None que é  usado para representar um não valor

'''
entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''
'''
#avaliação de curto circuito
print(True and False and True)
print(True and True and True)
print(True and 0 and True)
''''
'''
if 0 and 1:
    print(True and 1)
'''

# entrada = input('[E]ntrar ou [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# print(True and 0 and True)

#Operador lógico "not" usado para inverter expressões
#usado para inverter expressões
#not True = False
#not False = True 
print(not True)  #False
print(not False) #True

senha = input('Digite sua senha: ')

#if senha != '123456':
 #   print('Senha incorreta.')

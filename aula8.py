#Functions (funções)
#Parâmetros e Argumentos

#default = aquele que voçê  define valor MO PARAMETRO ex:def boas_vindas(nome='marcos', quantidade=6 ):
#non-default =  aquele que vc n define o valor no parametro ex:def boas_vindas(nome, quantidade ):
'''
def boas_vindas(nome='marcos', quantidade=6 ):
    print(f'ola {nome}.')
    print(f'temos {str(quantidade)} laptops em estoque')

boas_vindas(7)
'''

#print realiza uma tarefa
#return calcula e retorna um valor

'''
def cliente1(nome):
    print(f'olá, {nome}')

def cliente2(nome)
    return f'olá, {nome}'

x = cliente1('maria')
y = cliente2('genezio')

print(x)
print(y)
'''
'''
def soma(*numero):
    resultado = 0
    for num in numero:
        resultado += num
    return resultado

x = soma(2,3,4,7)

print(x)
'''
'''
#define função
def somador(valor1, valor2):
    soma = valor1 + valor2
    return soma
#chama função
res =  somador(3,4)
print(f'valor é: {res}'xxx)
      
#declaração da função

def imprime_msg(nomePessoa):
     print(f' O usuário {nomePessoa} escreveu uma mensagem')

#chamando a função
nome = input('Digite seu nome: ')
imprime_msg(nome)

'''

#criar uma função que armazena numeros e strings (dados)
#varios argumentos

def agencia(**carro):
     return carro

print(agencia(marca='gol'))
print(agencia(marca='fiat', cor='azul', moto=1))
print(agencia(marca='siena', cor='branca', motor=1, placa=1444))


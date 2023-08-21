#armazenar mais de uma informação em variaveis
#manter a sequencia dos dados em uma variavel
#o lower () método retorna um string onde todos os caracteres são minúsculos
#símbolos e números são ignorados
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho', 'roxo']

if cor_cliente.lower() in cores:
    print('sim')
else:
    print('não temos essa cor.')
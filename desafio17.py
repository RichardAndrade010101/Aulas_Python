#Solicitar a idade do usuário
idade = int(input('Digite sua idade: '))

#Verificar a faixa etária

if idade < 13:
    print('Você é uma criança.')

elif 13 <= idade <= 19:
    print('Você é um adolescente.')

else :
     print('Você é um adulto.')
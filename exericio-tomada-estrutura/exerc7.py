idade = int(input('digite sua idade '))

if idade < 13:
    print('você é uma criança')
elif idade < 18:
    print('você é um adolescente')
elif idade < 40:
    print('você é um adulto')
elif idade > 40:
    print('você é um idoso') 

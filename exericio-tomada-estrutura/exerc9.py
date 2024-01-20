numer = int(input('Digite um número maior que zero para inserir e zero se quiser sair '))
contP = 0
contI = 0

while numer < 0:
    numer = int(input('Digite um número maior que zero para inserir e zero se quiser sair '))
    

while numer > 0 :
    print('numero valido')   
    if numer % 2 == 0:
        print('par')
        contP += 1
    else:
        contI += 1
    numer = int(input('Digite um número maior que zero e zero se quiser sair '))
     
print('Quantidade de numero pares',contP)
print('Quantidade de numeros impares',contI)
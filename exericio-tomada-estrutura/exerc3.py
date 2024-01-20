nota = int(input('digite uma nota entre 0 e 10 '))


while nota < 0 or nota > 10:
    print('valor invalido')
    nota = int(input('digite uma nota entre 0 e 10 '))
    

print('A nota é {}'.format(nota))
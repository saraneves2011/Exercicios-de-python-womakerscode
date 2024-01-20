classifica = int(input('Digite sua pontuação de 0 a 10 '))

if classifica < 0 or classifica > 10:
    while classifica < 0 or classifica > 10:
        classifica = int(input('Digite sua pontuação de 0 a 10 '))
        if classifica >= 7 and classifica <= 10:
            print('Aluno aprovado')
        elif classifica < 7 and classifica >= 0:
            print('Aluno reprovado')    
elif classifica >= 7 and classifica <= 10:
    print('Aluno aprovado')
elif classifica >= 0:
    print('Aluno reprovado')  



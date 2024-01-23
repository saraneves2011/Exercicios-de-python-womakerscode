def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except (ZeroDivisionError,TypeError):
        print('Erro: impossivel dividir um valor por zero')
    except TypeError as e:
        print(f'Erro: dado informado não é válido {e}')
        

divisao(10,2)
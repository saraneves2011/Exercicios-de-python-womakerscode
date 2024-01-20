lado1 = int(input('digite o valor do comprimento '))
lado2 = int(input('digite o valor do comprimento '))
lado3 = int(input('digite o valor do comprimento '))

if lado1 == lado2 and lado2 == lado3:
    print('Triângulo equilatero')
elif  lado2 == lado3 and lado1 != lado3 or lado2 == lado1 and lado2 != lado3 or lado3 == lado1 and lado3 != lado2:
    print('Triângulo isosceles')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Triângulo escaleno')
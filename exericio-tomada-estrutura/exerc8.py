num1 = []
valor = 0
i = 0
while i < 3:
    nume = int(input('digite um numero '))
    num1.append(nume)
    i+=1

if num1[0] > num1[1]:
    valor = num1[0]
else:
    valor = num1[1]
    
if valor < num1[2]:
    valor = num1[2]
   
print('maior valor é',valor)

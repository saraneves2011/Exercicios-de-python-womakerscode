i = 0
vet = []
valor = 0

while i < 3:
    nu = int(input('Digite um valor '))
    vet.append(nu)
    i+=1
    
i = 0

while i < 2:
    if (vet[i] > vet[i+1]):
        valor = vet[i]
        vet[i] = vet[i+1]
        vet[i+1] = valor
    i+=1
i=0
while i < 2:
    if vet[i] > vet[i+1]:
        valor = vet[i]
        vet[i] = vet[i+1]
        vet[i+1] = valor
    i+=1

print(vet)
    
    
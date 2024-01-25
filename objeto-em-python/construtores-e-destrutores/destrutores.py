class MinhaClasse:
    def __init__(self,nome):
        self.nome = nome
        print(f'MinhaClasse:chamouoconstrutor padrao {nome}')
        
    def __del__(self):
        print(f'MinhaClasse: cgamou o destrutor de {self.nome}')
        
print('Começou a execução do programa')
objeto1 = MinhaClasse('objeto1')
#del objeto1
print('vai terminar o programa')
exit()
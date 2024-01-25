class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'Amarelo'
        self.modelo = 'Selta'
        self.velocidade = 50
    
    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def acelera(self):
        self.velocidade += 10
    
    def desacelera(self):
        self.velocidade -= 10
      
carro = Carro()
carro.liga()

print(f'Carro ligado ? {carro.ligado}')

carro.acelera()

for _ in range(1):
    carro.acelera
    
print(f'Velocidade do carro {carro.velocidade}km/h')

carro.desacelera()
for _ in range(5):
    carro.desacelera()

print(f'Velocidade do carro {carro.velocidade}km/h')

carro.desliga()
print(f'Carro ligado? {carro.ligado}')
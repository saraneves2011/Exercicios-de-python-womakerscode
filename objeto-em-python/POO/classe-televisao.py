class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        
    def ligar(self):
        self.ligada = True
        
    def desligar(self):
        self.desligar = False
        
    def mudar_canal_cima(self):
        if not self.ligada:
            return
        
        if self.canal < self.canal_max:
            self.canal += 1
            
    def mudar_canal_baixo(self):
        if not self.ligada:
            return
        if self.canal > self.canal_min:
            self.canal += -1
            
    def aumentar_volume_tv(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 10
        
    def diminuir_volume_tv(self):
        if not self.ligada:
            return
        
        if self.volume > self.volume_min:
            self.volume -= 10
    def __str__(self) -> str:
        return f'Televisão ligada {self.ligada} - Voolume {self.volume} - Canal {self.canal}'   
         
   
tv_sala = Televisao()
   
tv_sala.ligar()

for _ in range(3):
    tv_sala.aumentar_volume_tv()
    tv_sala.mudar_canal_baixo()

print(tv_sala.volume)
print(tv_sala.canal)
print(tv_sala.ligada)
print(tv_sala)


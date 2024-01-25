class Carro:
    def __init__(self,placa):
        self.placa = placa
        self.estacionado = False
        
    def estacionar(self):
        self.estacionado = True
    
    def sair_da_vaga(self):
        self.estacionado = False

class Moto:
    def __init__(self,placa):
        self.placa = placa
        self.estacionado = False
        
    def estacionar(self):
        self.estacionado = True
    
    def sair_da_vaga(self):
        self.estacionado = False
        
class Vaga:
    def __init__(self,identificador,tipo):
        self.id = identificador
        self.livre= True
        
        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vga {tipo} nõ foi reconhecido')
        
        self.tipo = tipo
        self.placa = None
        
    def ocupar(self,placa):
        if self.livre is False:
            raise ValueError(f'A vaga {self.identificador} já est´ocupada')
        
        self.placa = placa
        self.livre = False
    
    def desocupar(self):
        if self.livre is True:
            raise ValueError(f'a vaga{self.identificador} já está livre')
        
        self.placa= None
        self.livre = True
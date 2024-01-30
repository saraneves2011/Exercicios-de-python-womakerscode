from abc import ABC, abstractmethod
import random

class BaseContaCorrente(ABC):
    def __init__(self,nome,telefone,renda_mensal,gen):
        self.nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self.gen = gen
        self.saldo = 0
        self.conta = random.randint(1, 1001)
        self.valor_cheque_especial = 0
    
    @abstractmethod
    def saldos(self):
        pass
    
    @property    
    @abstractmethod
    def saque(self):
        pass
    
    @property
    @abstractmethod
    def deposito(self):
        pass
    
    @abstractmethod
    def saque_cheque_especial(self):
        pass
    

class ContaCorrenteDelas(BaseContaCorrente):
    def __init__(self,nome,telefone,renda_mensal,gen):
        super().__init__(nome,telefone,renda_mensal,gen)
    
    def imprime(self):
        print(f'nome: {self.nome} , telefone: {self._telefone} , conta: {self.conta}, renda: {self._renda_mensal} gen : {self.gen}')
        sald = int(input('para ver o saldo digite 1: '))
        if sald ==  1:
            self.saldos()
            
    def saldos(self):
        self.saldo = 1500
        print(self.saldo)
        opcao = int(input('Digite 1 para saque 2 para saque cheque especial 3 para deposito 4 para sair e 0 para voltar para menu anterior: '))
        if opcao == 1:
            self.saque
        if opcao == 2:
            self.saque_cheque_especial()
        if opcao == 3:
            self.deposito
        if opcao == 0:
            return self.imprime()
        
    def saque_cheque_especial(self):
        if self.gen == 'F':
            self.valor_cheque_especial = self._renda_mensal
            print(f'Valor do cheque especial {self.valor_cheque_especial}') 
            
            sacar = int(input('digite o valor que deseja sacar do cheque especial '))
            if sacar <= self.valor_cheque_especial:
                novo_valor_cheque = self.valor_cheque_especial - sacar
                print(novo_valor_cheque)
            else:
                print(f'Valor maior que o disponivel')
        else:
            print('Essa opção está disponicel somente para mulheres')               
    @property
    def saque(self):
        valor = int(input('digite valor pra saque '))
        self.saldo = self.saldo - valor
        return print(self.saldo)
    
    @property
    def deposito(self):
        valor = int(input('digite valor pra deposito '))
        self.saldo = self.saldo + valor
        return print(self.saldo)
    
    
            

contaNova = ContaCorrenteDelas('sara',"21548745",5000,'F')
contaNova.imprime()

contaNovaHomem = ContaCorrenteDelas('pedro','237865390',6000,'M')
contaNovaHomem.imprime()
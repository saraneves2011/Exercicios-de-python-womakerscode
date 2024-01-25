class MinhaClasse1:
     def __init__(self):
         print('MinhaClasse1: Chamou o construtor padrao')

class MinhaClasse2:
    pass


class MinhaClasse3:
    def __init__(self,param):
        print(f'MinhaClasse3: chamou o construtor parametrizado {param}')         

MinhaClasse1()
MinhaClasse3('meu objeto')
class Pessoa:
    def __init__(self,nome):
        self._nome = nome
        self._tipo = 'Pessoa'
    
    def falar_oi(self):
        print(f'oi,meu nome é {self._nome}')
        
    def falar_tipo(self):
        print(f'Meu tipo {self._tipo}')
        
pessoa = Pessoa('Naira')
pessoa.falar_oi()
pessoa.falar_tipo()
print()

class Estudante(Pessoa):
    def __init__(self,nome,curso):
        super().__init__(nome)
        self._curso = curso
        
    def falar_curso(self):
        print(f'Eu {self._nome},estudo o curso {self._curso}')

    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()

estudante = Estudante('Yasmin','Introdução ao python')
estudante.falar_oi()
estudante.falar_tipo()
estudante.falar_curso()

print('O objeto estudante é uma instancia da classe estudante?',isinstance(estudante,Estudante))
print('O objeto estudante é uma instancia da classe pessoa?',isinstance(estudante,Pessoa))
print('A classe Estudante é uma subclasse de Pessoa?',issubclass(Estudante,Pessoa))

class Trabalhador(Pessoa):
    def __init__(self,nome,profissao):
        super().__init__(nome)
        self.__profissao = profissao
        self._tipo = 'Trabalhador'
    
    def falar_prof(self):
        print(f'Eu { self._nome} trabalho como {self.__profissao}')
        
    def falar_tipo(self):
        return super().falar_tipo()
    
trabalhador = Trabalhador('Edson','Engenheiro')
trabalhador.falar_oi()
trabalhador.falar_prof()
trabalhador.falar_tipo()
print()
    
class Professor(Trabalhador):
    def __init__(self,nome,disciplina):
        super().__init__(nome,'Professor')
        self.__disciplina = disciplina
    
    def falar_prof(self):
        self.__profissao = 'Instrutor'
        return super().falar_prof()
    
    def falar_disc(self):
        print(f'Eu {self._nome} dou a disciplina {self.__disciplina}')
        
    def falar_tipo(self):
        self._tipo = 'Professor'
        return super().falar_tipo()    
    
professor = Professor('Diego','Lógica')
professor.falar_oi()
professor.falar_prof()
professor.falar_disc()
professor.falar_tipo()
print()


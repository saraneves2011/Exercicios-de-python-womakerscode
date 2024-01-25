class Pessoa:
    def __init__(self,nome,profissao,identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade
    def __str__(self) -> str:
        return f'Nome:{self._nome},Profissao:{self.profissao}, identidae: {self.__identidade}'

pessoal = Pessoa('Marta Lima','Estudante','12345')
print(pessoal)
print()

pessoal.profissao = 'Programadora'
print(pessoal)
print()

pessoal._nome = 'Marta'
print(pessoal)
print()

pessoal.__identidade = '2346'
print(pessoal)
print()
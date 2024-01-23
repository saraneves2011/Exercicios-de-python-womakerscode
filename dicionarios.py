dicionario = {}

dicionario['maçã'] = 'é uma fruta'
dicionario['carro'] = 'é um veículo'

num =  int(input('digite seu numero'))

dicionario.update({'numero':num})
print(dicionario)
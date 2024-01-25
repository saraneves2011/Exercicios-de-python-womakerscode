bebida = 'refrigerante'
def cardapio():
    global bebida # issosiginifica que a variaveldefinida fora desse escopo vai ser modificada
    comida = 'hamburguer'
    bebida='suco'
    print(comida)
    print(bebida)
    
cardapio()
print(bebida)
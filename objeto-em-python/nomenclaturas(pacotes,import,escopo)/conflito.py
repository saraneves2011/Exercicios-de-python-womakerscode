from funcoes_log import *

#pelo que eu entendi se vc importar tudo do outro arquivo e criar uma nova função com o mesmo nome oprograama vaia ceitar e não vaai mostrar erro 
#por isso é importante importar valores especificos 

imprimir_no_log(f'Bem vinda,{nome_usuario}')

def imprimir_no_log(texto):
    print(texto)
    
imprimir_no_log(f'Bem vinda, {nome_usuario}')
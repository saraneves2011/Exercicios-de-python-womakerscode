import colorama

colorama.init()


nome_usuario = 'Dori'

def imprimir_no_log(texto,nivel='info'):
    if nivel.lower() == 'info':
        print(colorama.Fore.LIGHTBLUE_EX + f'Info: ',end='')
        print(colorama.Style.RESET_ALL + texto)
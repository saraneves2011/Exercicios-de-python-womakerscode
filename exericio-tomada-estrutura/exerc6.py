login = input('login: ')
senha = input('senha: ')

while login != 'admin' and senha != 'admin123':
    print('Erro ao fazer login digite o usuario e senha novamente')
    login = input('login: ')
    senha = input('senha: ')
    if(login == 'admin' and senha == 'admin123'):
        print('LOGADO!!!')
    


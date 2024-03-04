def introduction_page():
    message = '''
        Sistema Cadastral

        * Cadastrar Cliente - 1
        * Buscar Cliente Por Nome - 2
        * Cadastrar Loja - 3
        * Sair - 5
    '''

    print(message)
    command = input('Comando: ')

    return command
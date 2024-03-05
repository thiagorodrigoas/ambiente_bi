def introduction_page():
    message = '''
        Sistema Cadastral

        * Cadastrar Cliente - 1
        * Buscar Cliente Por Nome - 2

        * Cadastrar Loja - 3
        * Buscar Loja Por Nome - 4

        * Cadastrar Produto - 5
        * Buscar Produto Por Nome - 6

        * Cadastrar Vendedor - 7
        * Buscar Vendedor Por Nome - 8

        * Sair - 0
    '''

    print(message)
    command = input('Comando: ')

    return command
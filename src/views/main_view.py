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

        * Cadastrar Estoque - 9
        #* Buscar Estoque Por Loja - 10

        #* Cadastrar Venda - 11
        #* Buscar Venda Por Vendedor - 12

        #* Cadastrar Item Venda - 13
        #* Buscar Item Venda Por Venda - 14

        * Sair - 0
    '''

    print(message)
    command = input('Comando: ')

    return command
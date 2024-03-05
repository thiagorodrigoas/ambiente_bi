from .constructor.introduction_process import introduction_process
from .constructor.cliente_registro_constructor import cliente_cadastro_constructor
from .constructor.cliente_encontra_constructor import cliente_encontra_constructor

from .constructor.loja_registro_constructor import loja_cadastro_constructor
from .constructor.loja_encontra_constructor import loja_encontra_constructor

from .constructor.produto_registro_constructor import produto_cadastro_constructor
from .constructor.produto_encontra_constructor import produto_encontra_constructor

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': cliente_cadastro_constructor()
        elif command == '2': cliente_encontra_constructor()
        elif command == '3': loja_cadastro_constructor()
        elif command == '4': loja_encontra_constructor()
        elif command == '5': produto_cadastro_constructor()
        elif command == '6': produto_encontra_constructor()
        elif command == '0': exit()
        else: print('\n Comando nao encontrado!! \n\n')
    
from .constructor.introduction_process import introduction_process
from .constructor.cliente_registro_contructor import cliente_cadastro_constructor
#from .constructor.people_finder_constructor import people_finder_constructor

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': cliente_cadastro_constructor()
        #elif command == '2': people_finder_constructor()
        elif command == '5': exit()
        else: print('\n Comando nao encontrado!! \n\n')
    
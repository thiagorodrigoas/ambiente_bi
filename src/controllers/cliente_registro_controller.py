from typing import Dict
from src.models.repository.cliente_repository import ClienteRepository
from src.models.entities.cliente import Cliente

class ClienteRegistroController:
    def register(self, info_cliente_novo: Dict) -> Dict:
        try:
            self.__validate_fields(info_cliente_novo)
            self.__insere_entidade_cliente(info_cliente_novo)
            response = self.__format_response(info_cliente_novo)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __validate_fields(self, info_cliente_novo: Dict) -> None:
        if not isinstance(info_cliente_novo["des_nome"], str):
            raise Exception('Campo Nome Incorreto!')

        # try: int(info_cliente_novo["age"])
        # except: raise Exception('Campo Idade Incorreto!')

        # try: int(info_cliente_novo["height"])
        # except: raise Exception('Campo Altura Incorreto!')

    def __insere_entidade_cliente(self, info_cliente_novo: Dict) -> None:
        des_nome = info_cliente_novo['des_nome']
        des_sobrenome = info_cliente_novo['des_sobrenome']
        vlr_poder_compra = info_cliente_novo['vlr_poder_compra']
        vlr_saldo = info_cliente_novo['vlr_saldo']
        des_email = info_cliente_novo['des_email']
        num_telefone = info_cliente_novo['num_telefone']
        dat_nascimento = info_cliente_novo['dat_nascimento']
        dat_cadastro = info_cliente_novo['dat_cadastro']

        novo_cliente = Cliente(des_nome=des_nome, 
                               des_sobrenome=des_sobrenome, 
                               vlr_poder_compra=vlr_poder_compra, 
                               vlr_saldo=vlr_saldo, 
                               des_email=des_email, 
                               num_telefone=num_telefone, 
                               dat_nascimento=dat_nascimento, 
                               dat_cadastro=dat_cadastro
                               )
        #FIXME: PORQUE TENHO QUE COLOCAR O SELF PRA CHAMAR? SE TIRAR O SELF APRESENTA O ERRO: insert() missing 1 required positional argument: 'self'
        ClienteRepository.insert(self, cliente = novo_cliente)

    def __format_response(self, info_cliente_novo: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Cliente",
            "attributes": info_cliente_novo
        }
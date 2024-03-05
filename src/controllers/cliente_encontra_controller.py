from typing import Dict
from src.models.repository.cliente_repository import ClienteRepository
from src.models.entities.cliente import Cliente

class ClienteEcontraController:
    def encontra(self, info_cliente_busca: Dict) -> Dict:
        try:
            self.__validate_fields(info_cliente_busca)
            cliente = self.__busca_cliente(info_cliente_busca)
            response = self.__format_response(cliente)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }
        
    def __validate_fields(self, info_cliente_busca: Dict) -> None:
        if not isinstance(info_cliente_busca["des_nome"], str):
            raise Exception('Campo Nome Incorreto!')

    def __busca_cliente(self, info_cliente_busca):

        cliente = ClienteRepository.select_where(self, info_cliente_busca)
        return cliente

    def __format_response(self, info_cliente_busca: Cliente) -> Dict:
            return {
                "count": 1,
                "type": "Cliente",
                "attributes": 
                    {   "des_nome": info_cliente_busca.des_nome,
                        "des_sobrenome": info_cliente_busca.des_sobrenome,
                        "vlr_poder_compra": info_cliente_busca.vlr_poder_compra,
                        "vlr_saldo": info_cliente_busca.vlr_saldo,
                        "des_email": info_cliente_busca.des_email,
                        "num_telefone": info_cliente_busca.num_telefone,
                        "dat_nascimento": info_cliente_busca.dat_nascimento,
                        "dat_cadastro": info_cliente_busca.dat_cadastro
                    }
            }
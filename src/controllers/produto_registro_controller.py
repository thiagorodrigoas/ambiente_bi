from typing import Dict
from src.models.repository.produto_repository import ProdutoRepository
from src.models.entities.produto import Produto

class ProdutoRegistroController:
    def register(self, info_produto_novo: Dict) -> Dict:
        try:
            self.__validate_fields(info_produto_novo)
            self.__insere_entidade_produto(info_produto_novo)
            response = self.__format_response(info_produto_novo)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __validate_fields(self, info_produto_novo: Dict) -> None:
        if not isinstance(info_produto_novo["nom_produto"], str):
            raise Exception('Campo Nome Incorreto!')

        # try: int(info_produto_novo["age"])
        # except: raise Exception('Campo Idade Incorreto!')

        # try: int(info_produto_novo["height"])
        # except: raise Exception('Campo Altura Incorreto!')

    def __insere_entidade_produto(self, info_produto_novo: Dict) -> None:
        nom_produto= info_produto_novo['nom_produto']
        vlr_custo= info_produto_novo['vlr_custo']
        des_produto= info_produto_novo['des_produto']
        des_ticket_price= info_produto_novo['des_ticket_price']
        dat_criacao= info_produto_novo['dat_criacao']
        dat_alteracao= info_produto_novo['dat_alteracao'] 

        novo_produto = Produto(
                nom_produto= nom_produto,
                vlr_custo= vlr_custo,
                des_produto= des_produto,
                des_ticket_price= des_ticket_price,
                dat_criacao= dat_criacao,
                dat_alteracao= dat_alteracao
            )
        #FIXME: PORQUE TENHO QUE COLOCAR O SELF PRA CHAMAR? SE TIRAR O SELF APRESENTA O ERRO: insert() missing 1 required positional argument: 'self'
        ProdutoRepository.insert(self, produto = novo_produto)

    def __format_response(self, info_produto_novo: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Produto",
            "attributes": info_produto_novo
        }
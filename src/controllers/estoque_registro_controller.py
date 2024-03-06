from typing import Dict
from src.models.repository.estoque_repository import EstoqueRepository
from src.models.repository.loja_repository import LojaRepository
from src.models.repository.produto_repository import ProdutoRepository
from src.models.entities.estoque import Estoque


class EstoqueCadastroController:
    def cadastra(self, info_estoque: Dict) -> Dict:
        try:
            self.__validate_fields(info_estoque)
            self.__registra_estoque(info_estoque)
            response = self.__format_response(info_estoque)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def busca_lojas():
        lojas = LojaRepository.select()
        return lojas  
     
    def busca_produtos():
        produtos = ProdutoRepository.select()
        return produtos  

    def __validate_fields(self, info_estoque: Dict) -> None:
        pass
        # if not info_estoque.get("nom_vendedor"):
        #     raise Exception('O nome do vendedor é obrigatório!')

    def __registra_estoque(self, info_estoque: Dict) -> Estoque:
        novo_estoque = Estoque(
        cod_loja= info_estoque['cod_loja'],
        cod_produto= info_estoque['cod_produto'],
        qtd_produto= info_estoque['qtd_produto'],
        dat_criacao= info_estoque['dat_criacao'],
        dat_alteracao= info_estoque['dat_alteracao']
        )
        EstoqueRepository.insert(self, estoque = novo_estoque)
        return novo_estoque

    def __format_response(self, info_estoque: Dict) -> Dict:
        return {
            "type": "Estoque",
            "count": 1,
            "attributes": info_estoque
        }

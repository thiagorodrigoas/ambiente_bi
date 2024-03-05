from typing import Dict
from src.models.repository.produto_repository import ProdutoRepository
from src.models.entities.produto import Produto

class ProdutoEncontraController:
    def encontra(self, info_produto_busca: Dict) -> Dict:
        try:
            self.__validate_fields(info_produto_busca)
            produto = self.__busca_produto(info_produto_busca)
            response = self.__format_response(produto)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }
        
    def __validate_fields(self, info_produto_busca: Dict) -> None:
        if not isinstance(info_produto_busca["nom_produto"], str):
            raise Exception('Campo Nome do Produto Incorreto!')

    def __busca_produto(self, info_produto_busca):

        produto = ProdutoRepository.select_where(self, info_produto_busca)
        return produto

    def __format_response(self, info_produto_busca: Produto) -> Dict:
            return {
                "count": 1,
                "type": "Produto",
                "attributes": 
                    {   "nom_produto": info_produto_busca.nom_produto,
                        "vlr_custo": info_produto_busca.vlr_custo,
                        "des_produto": info_produto_busca.des_produto,
                        "des_ticket_price": info_produto_busca.des_ticket_price,
                        "dat_criacao": info_produto_busca.dat_criacao,
                        "dat_alteracao": info_produto_busca.dat_alteracao
                    }
            }

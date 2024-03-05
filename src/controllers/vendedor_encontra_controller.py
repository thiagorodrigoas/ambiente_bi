from typing import Dict
from src.models.repository.vendedor_repository import VendedorRepository
from src.models.entities.vendedor import Vendedor

class VendedorEncontraController:
    def encontra(self, info_vendedor_busca: Dict) -> Dict:
        try:
            self.__validate_fields(info_vendedor_busca)
            vendedor = self.__busca_vendedor(info_vendedor_busca)
            response = self.__format_response(vendedor)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def __validate_fields(self, info_vendedor_busca: Dict) -> None:
        if not isinstance(info_vendedor_busca["nom_vendedor"], str):
            raise Exception('Campo nome do vendedor incorreto!')

    def __busca_vendedor(self, info_vendedor_busca: Dict) -> Vendedor:
        vendedor = VendedorRepository.select_where(self, info_vendedor_busca)
        return vendedor

    def __format_response(self, vendedor: Vendedor) -> Dict:
            return {
                "count": 1,
                "type": "Vendedor",
                "attributes": {
                    "nom_vendedor": vendedor.nom_vendedor,
                    "des_email": vendedor.des_email,
                    "cod_loja": vendedor.cod_loja,
                    "dat_criacao": vendedor.dat_criacao,
                    "dat_alteracao": vendedor.dat_alteracao
                }
            }

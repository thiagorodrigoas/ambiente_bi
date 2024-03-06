from typing import Dict
from src.models.repository.vendedor_repository import VendedorRepository
from src.models.repository.loja_repository import LojaRepository
from src.models.entities.vendedor import Vendedor


class VendedorCadastroController:
    def cadastra(self, info_vendedor: Dict) -> Dict:
        try:
            self.__validate_fields(info_vendedor)
            self.__registra_vendedor(info_vendedor)
            response = self.__format_response(info_vendedor)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def busca_lojas():
        lojas = LojaRepository.select()
        return lojas  
     
    def __validate_fields(self, info_vendedor: Dict) -> None:
        if not info_vendedor.get("nom_vendedor"):
            raise Exception('O nome do vendedor é obrigatório!')

    def __registra_vendedor(self, info_vendedor: Dict) -> Vendedor:
        novo_vendedor = Vendedor(
        nom_vendedor =info_vendedor['nom_vendedor'],
        des_email =info_vendedor['des_email'],
        cod_loja =info_vendedor['cod_loja'],
        dat_criacao =info_vendedor['dat_criacao'],
        dat_alteracao =info_vendedor['dat_alteracao']
        )
        VendedorRepository.insert(self, vendedor= novo_vendedor)
        return novo_vendedor

    def __format_response(self, info_vendedor: Dict) -> Dict:
        return {
            "type": "Vendedor",
            "count": 1,
            "attributes": info_vendedor
        }

from typing import Dict
from src.models.repository.loja_repository import LojaRepository
from src.models.entities.loja import Loja

class LojaEncontraController:
    def encontra(self, info_loja_busca: Dict) -> Dict:
        try:
            self.__validate_fields(info_loja_busca)
            loja = self.__busca_loja(info_loja_busca)
            response = self.__format_response(loja)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }
        
    def __validate_fields(self, info_loja_busca: Dict) -> None:
        if not isinstance(info_loja_busca["nom_loja"], str):
            raise Exception('Campo Nome da Loja Incorreto!')

    def __busca_loja(self, info_loja_busca):
        loja = LojaRepository.select_where(self, info_loja_busca)
        return loja

    def __format_response(self, loja: Loja) -> Dict:
        return {
            "count": 1,
            "type": "Loja",
            "attributes": { 
                "nom_loja": loja.nom_loja,
                "cod_long": loja.cod_long,
                "cod_lat": loja.cod_lat,
                "des_bairro": loja.des_bairro,
                "des_pais": loja.des_pais,
                "des_estado": loja.des_estado,
                "des_tamanho_loja": loja.des_tamanho_loja,
                "dat_criacao": loja.dat_criacao,
                "dat_alteracao": loja.dat_alteracao
            }
        }

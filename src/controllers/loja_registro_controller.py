from typing import Dict
from src.models.repository.loja_repository import LojaRepository
from src.models.entities.loja import Loja

class LojaRegistroController:
    def register(self, info_loja_nova: Dict) -> Dict:
        try:
            self.__validate_fields(info_loja_nova)
            self.__insere_entidade_loja(info_loja_nova)
            response = self.__format_response(info_loja_nova)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __validate_fields(self, info_loja_nova: Dict) -> None:
        if not isinstance(info_loja_nova["nom_loja"], str):
            raise Exception('Campo Nome Incorreto!')

        # try: int(info_loja_nova["age"])
        # except: raise Exception('Campo Idade Incorreto!')

        # try: int(info_loja_nova["height"])
        # except: raise Exception('Campo Altura Incorreto!')

    def __insere_entidade_loja(self, info_loja_nova: Dict) -> None:
        nom_loja = info_loja_nova['nom_loja']
        cod_long = info_loja_nova['cod_long']
        cod_lat = info_loja_nova['cod_lat']
        des_bairro = info_loja_nova['des_bairro']
        des_pais = info_loja_nova['des_pais']
        des_estado = info_loja_nova['des_estado']
        des_tamanho_loja = info_loja_nova['des_tamanho_loja']
        dat_criacao = info_loja_nova['dat_criacao']
        dat_alteracao = info_loja_nova['dat_alteracao']

        nova_loja = Loja(
            nom_loja= nom_loja,
            cod_long= cod_long,
            cod_lat= cod_lat,
            des_bairro= des_bairro,
            des_pais= des_pais,
            des_estado= des_estado,
            des_tamanho_loja= des_tamanho_loja,
            dat_criacao= dat_criacao,
            dat_alteracao= dat_alteracao
            )
        #FIXME: PORQUE TENHO QUE COLOCAR O SELF PRA CHAMAR? SE TIRAR O SELF APRESENTA O ERRO: insert() missing 1 required positional argument: 'self'
        LojaRepository.insert(self, loja = nova_loja)

    def __format_response(self, info_loja_nova: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Loja",
            "attributes": info_loja_nova
        }
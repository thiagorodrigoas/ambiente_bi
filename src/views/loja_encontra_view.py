import os
from typing import Dict

class LojaEncontraView:
    def encontra_loja_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Loja \n\n')
        nom_loja = input('Determine o nome da loja para busca: ')

        info_encontra_loja = {
            "nom_loja": nom_loja
        }

        return info_encontra_loja

    def encontra_loja_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Loja encontrada com sucesso!

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome: {message["attributes"]["nom_loja"]}
                Longitude: {message["attributes"]["cod_long"]}
                Latitude: {message["attributes"]["cod_lat"]}
                Bairro: {message["attributes"]["des_bairro"]}
                País: {message["attributes"]["des_pais"]}
                Estado: {message["attributes"]["des_estado"]}
                Tamanho da Loja: {message["attributes"]["des_tamanho_loja"]}
                Data de Criação: {message["attributes"]["dat_criacao"]}
                Data de Alteração: {message["attributes"]["dat_alteracao"]}
        '''
        print(success_message)

    def encontra_loja_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar loja!

            Erro: {error}
        '''
        print(fail_message)

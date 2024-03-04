import os
from typing import Dict

from fakes import faker

class LojaCadastroView:
    def cadastro_loja_view(self):
        os.system('cls||clear')
        
        l = faker.Loja()

        print('Cadastrar Nova Loja \n\n')
        nom_loja = l.nom_loja # input('nom_loja: ')
        cod_long = l.cod_long # input('cod_long: ')
        cod_lat = l.cod_lat # input('cod_lat: ')
        des_bairro = l.des_bairro # input('des_bairro: ')
        des_pais = l.des_pais # input('des_pais: ')
        des_estado = l.des_estado # input('des_estado: ')
        des_tamanho_loja = l.des_tamanho_loja # input('des_tamanho_loja: ')
        dat_criacao = l.dat_criacao # input('dat_criacao: ')
        dat_alteracao = l.dat_alteracao # input('dat_alteracao: ')
        
        info_loja = {
            'nom_loja': nom_loja,
            'cod_long': cod_long,
            'cod_lat': cod_lat,
            'des_bairro': des_bairro,
            'des_pais': des_pais,
            'des_estado': des_estado,
            'des_tamanho_loja': des_tamanho_loja,
            'dat_criacao': dat_criacao,
            'dat_alteracao': dat_alteracao

        }
        return info_loja
    

    def cadastro_loja_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Loja cadastrada com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["nom_loja"] }
                Longitude: { message["attributes"]["cod_long"] }
                Latitude: { message["attributes"]["cod_lat"] }
                Bairro: { message["attributes"]["des_bairro"] }
                Pais: { message["attributes"]["des_pais"] }
                Estado: { message["attributes"]["des_estado"] }
                Tamanho Loja: { message["attributes"]["des_tamanho_loja"] }
                Data criacao: { message["attributes"]["dat_criacao"] }
                Data alteracao: { message["attributes"]["dat_alteracao"] }
        '''
        print(success_message)


    def cadastro_loja_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar Loja!

            Erro: { error }
        '''
        print(fail_message)
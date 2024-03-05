import os
from typing import Dict

class VendedorEncontraView:
    def encontra_vendedor_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Vendedor \n\n')
        nom_vendedor = input('Informe o nome do vendedor para a busca: ')
        #des_email = input('Informe o e-mail do vendedor para a busca (opcional): ')

        info_encontra_vendedor = {
            "nom_vendedor": nom_vendedor
        #    "des_email": des_email
        }

        return info_encontra_vendedor

    def encontra_vendedor_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Vendedor encontrado com sucesso!
            Produto encontrado com sucesso!

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome: {message["attributes"]["nom_vendedor"]}
                E-mail: {message["attributes"]["des_email"]}
                Loja: {message["attributes"]["cod_loja"]}
                Data de Criação: {message["attributes"]["dat_criacao"]}
                Data de Alteração: {message["attributes"]["dat_alteracao"]}
        '''
        print(success_message)

    def encontra_vendedor_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar vendedor!

            Erro: {error}
        '''
        print(fail_message)

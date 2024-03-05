import os
from typing import Dict

class ProdutoEncontraView:
    def encontra_produto_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Produto \n\n')
        nom_produto = input('Determine o nome do produto para busca: ')

        info_encontra_produto = {
            "nom_produto": nom_produto
        }

        return info_encontra_produto

    def encontra_produto_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Produto encontrado com sucesso!

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome Produto: {message["attributes"]["nom_produto"]}
                Valor custo: {message["attributes"]["vlr_custo"]}
                Descrição: {message["attributes"]["des_produto"]}
                Ticket ação: {message["attributes"]["des_ticket_price"]}
                Data criação: {message["attributes"]["dat_criacao"]}
                Data alteração: {message["attributes"]["dat_alteracao"]}
        '''
        print(success_message)

    def encontra_produto_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar produto!

            Erro: {error}
        '''
        print(fail_message)

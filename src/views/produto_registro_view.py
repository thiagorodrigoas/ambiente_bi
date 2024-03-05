import os
from typing import Dict

from fakes import faker

class ProdutoCadastroView:
    def cadastro_produto_view(self):
        os.system('cls||clear')
        
        p = faker.Produto()

        print('Cadastrar Novo Produto \n\n')
        nom_produto = p.nom_produto # input('nom_produto: ')
        vlr_custo = p.vlr_custo # input('vlr_custo: ')
        des_produto = p.des_produto # input('des_produto: ')
        des_ticket_price = p.des_ticket_price # input('des_ticket_price: ')
        dat_criacao = p.dat_criacao # input('dat_criacao: ')
        dat_alteracao = p.dat_alteracao # input('dat_alteracao: ')

        info_produto = {
                'nom_produto': nom_produto,
                'vlr_custo': vlr_custo,
                'des_produto': des_produto,
                'des_ticket_price': des_ticket_price,
                'dat_criacao': dat_criacao,
                'dat_alteracao': dat_alteracao
        }
        return info_produto
    

    def cadastro_produto_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Produto cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                'Nome Produto': { message["attributes"]["nom_produto"] },
                'Valor custo': { message["attributes"]["vlr_custo"] },
                'Descrição': { message["attributes"]["des_produto"] },
                'Ticket ação': { message["attributes"]["des_ticket_price"] },
                'Data criacao': { message["attributes"]["dat_criacao"] },
                'Data alteracao': { message["attributes"]["dat_alteracao"] }
        '''
        print(success_message)


    def cadastro_produto_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar Produto!

            Erro: { error }
        '''
        print(fail_message)
import os
from typing import Dict
from src.utilities.faker_providers import faker

import random

class EstoqueCadastroView:
    def __init__(self, lojas, produtos) -> None:
        self.lojas = lojas
        self.produtos = produtos

    def cadastro_estoque_view(self) -> Dict:
        os.system('cls||clear')
        

        print('Selecione qual loja.')
        lista_loja = [loja.cod_id_loja for loja in self.lojas]
        print(lista_loja)
        loja = random.choice(self.lojas) #v.cod_loja  # input('Código Loja: ')

        print('Selecione qual produto será incluido.')
        lista_produto = [produto.cod_id_produto for produto in self.produtos]
        print(lista_produto)
        produto = random.choice(self.produtos) #v.cod_loja  # input('Código Loja: ')

        print('Cadastrar Novo Estoque \n\n')
        e = faker.Estoque(loja, produto)
        cod_loja = e.cod_loja # input('cod_loja: ')
        cod_produto = e.cod_produto # input('cod_produto: ')
        qtd_produto = e.qtd_produto # input('qtd_produto: ')
        dat_criacao = e.dat_criacao # input('dat_criacao: ')
        dat_alteracao = e.dat_alteracao # input('dat_alteracao: ')

        info_estoque = {
            'cod_loja': cod_loja,
            'cod_produto': cod_produto,
            'qtd_produto': qtd_produto,
            'dat_criacao': dat_criacao,
            'dat_alteracao': dat_alteracao
        }
        return info_estoque

    def cadastro_estoque_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')
        print(f'''Estoque cadastrado com sucesso!
            Cod. Loja: {message["attributes"]["cod_loja"]}
            Cod. Produto: {message["attributes"]["cod_produto"]}
            Qtde. Produto: {message["attributes"]["qtd_produto"]}
            Data Criação: {message["attributes"]["dat_criacao"]}
            Data Alteração: {message["attributes"]["dat_alteracao"]}''')

    def cadastro_estoque_falha(self, error: str) -> None:
        os.system('cls||clear')
        print(f'Falha ao cadastrar estoque!\nErro: {error}')

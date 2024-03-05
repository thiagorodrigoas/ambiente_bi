import os
from typing import Dict
from src.utilities.faker_providers import faker

import random

class VendedorCadastroView:
    def __init__(self, lojas) -> None:
        self.lojas = lojas

    def cadastro_vendedor_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Novo Vendedor \n\n')
        v = faker.Vendedor()

        nom_vendedor = v.nom_vendedor  # input('Nome Vendedor: ')
        des_email = v.des_email  # input('Email: ')
        dat_criacao = v.dat_criacao  # input('Data de Criação: ')
        dat_alteracao = v.dat_alteracao  # input('Data de Alteração: ')

        print('Alocar vendedor em qual loja?')
        lista_loja = [loja.cod_id_loja for loja in self.lojas]
        print(lista_loja)
        cod_loja = random.choice(lista_loja) #v.cod_loja  # input('Código Loja: ')
        
        info_vendedor = {
            'nom_vendedor': nom_vendedor,
            'des_email': des_email,
            'cod_loja': cod_loja,
            'dat_criacao': dat_criacao,
            'dat_alteracao': dat_alteracao
        }
        return info_vendedor

    def cadastro_vendedor_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')
        print(f'''Vendedor cadastrado com sucesso!
            Nome: {message["attributes"]["nom_vendedor"]}
            Email: {message["attributes"]["des_email"]}
            Loja: {message["attributes"]["cod_loja"]}
            Data Criação: {message["attributes"]["dat_criacao"]}
            Data Alteração: {message["attributes"]["dat_alteracao"]}''')

    def cadastro_vendedor_falha(self, error: str) -> None:
        os.system('cls||clear')
        print(f'Falha ao cadastrar vendedor!\nErro: {error}')

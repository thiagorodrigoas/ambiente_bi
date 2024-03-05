import os
from typing import Dict

from utilities.faker_providers import faker

class ClienteCadastroView:
    def cadastro_cliente_view(self):
        os.system('cls||clear')
        
        c = faker.Cliente()

        print('Cadastrar Nova Pessoa \n\n')
        des_nome = c.des_nome #  input('des_nome: ')
        des_sobrenome = c.des_sobrenome #  input('des_sobrenome: ')
        vlr_poder_compra = c.vlr_poder_compra #  input('vlr_poder_compra: ')
        vlr_saldo = c.vlr_saldo #  input('vlr_saldo: ')
        des_email = c.des_email #  input('des_email: ')
        num_telefone = c.num_telefone #  input('num_telefone: ')
        dat_nascimento = c.dat_nascimento #  input('dat_nascimento: ')
        dat_cadastro = c.dat_cadastro #  input('dat_cadastro: ')
        
        info_cliente = {'des_nome' : des_nome,
                        'des_sobrenome' : des_sobrenome,
                        'vlr_poder_compra' : vlr_poder_compra,
                        'vlr_saldo' : vlr_saldo,
                        'des_email' : des_email,
                        'num_telefone' : num_telefone,
                        'dat_nascimento' : dat_nascimento,
                        'dat_cadastro' : dat_cadastro}
        return info_cliente
    

    def cadastro_cliente_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuario cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["des_nome"] }
                Sobrenome: { message["attributes"]["des_sobrenome"] }
                Poder de compra: { message["attributes"]["vlr_poder_compra"] }
                Saldo: { message["attributes"]["vlr_saldo"] }
                Email: { message["attributes"]["des_email"] }
                Telefone: { message["attributes"]["num_telefone"] }
                Data Nascimento: { message["attributes"]["dat_nascimento"] }
                Data Cadastro: { message["attributes"]["dat_cadastro"] }
        '''
        print(success_message)


    def cadastro_cliente_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar usuario!

            Erro: { error }
        '''
        print(fail_message)
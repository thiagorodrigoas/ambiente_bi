import os
from typing import Dict

class ClienteEncontraView:
    def encontra_cliente_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Cliente \n\n')
        des_nome = input('Determine o nome da pessoa para busca: ')

        info_encontra_cliente = {
            "des_nome": des_nome
        }

        return info_encontra_cliente

    def encontra_cliente_sucesso(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Cliente encontrado com sucesso!

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

    def encontra_cliente_falha(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao encontrar cliente!

            Erro: { error }
        '''
        print(fail_message)
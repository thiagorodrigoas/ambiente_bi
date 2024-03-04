from src.views.cliente_registro_view import ClienteCadastroView
from src.controllers.cliente_registro_controller import ClienteRegistroController

def cliente_cadastro_constructor():
    cliente_cadastro_view = ClienteCadastroView()
    cliente_registro_controller = ClienteRegistroController()

    info_cliente_novo = cliente_cadastro_view.cadastro_cliente_view()
    response = cliente_registro_controller.register(info_cliente_novo)

    if response["success"]:
        cliente_cadastro_view.cadastro_cliente_sucesso(response["message"])
    else:
        cliente_cadastro_view.cadastro_cliente_falha(response["error"])
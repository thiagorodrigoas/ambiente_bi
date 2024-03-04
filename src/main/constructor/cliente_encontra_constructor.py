from src.views.cliente_encontra_view import ClienteEncontraView
from src.controllers.cliente_encontra_controller import ClienteEcontraController

def cliente_encontra_constructor():
    cliente_encontra_view = ClienteEncontraView()
    cliente_encontra_controller = ClienteEcontraController()

    info_cliente_busca = cliente_encontra_view.encontra_cliente_view()
    response = cliente_encontra_controller.encontra(info_cliente_busca)

    if response["success"]:
        cliente_encontra_view.encontra_cliente_sucesso(response["message"])
    else:
        cliente_encontra_view.encontra_cliente_falha(response["error"])
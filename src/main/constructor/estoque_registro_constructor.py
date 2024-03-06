from src.views.estoque_registro_view import EstoqueCadastroView
from src.controllers.estoque_registro_controller import EstoqueCadastroController

def estoque_registro_constructor():
    lojas = EstoqueCadastroController.busca_lojas()  
    produtos = EstoqueCadastroController.busca_produtos()  
    estoque_registro_view = EstoqueCadastroView(lojas, produtos)
    estoque_registro_controller = EstoqueCadastroController()

    info_estoque = estoque_registro_view.cadastro_estoque_view()
    response = estoque_registro_controller.cadastra(info_estoque)

    if response["success"]:
        estoque_registro_view.cadastro_estoque_sucesso(response["message"])
    else:
        estoque_registro_view.cadastro_estoque_falha(response["error"])

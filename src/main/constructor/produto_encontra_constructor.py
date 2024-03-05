from src.views.produto_encontra_view import ProdutoEncontraView
from src.controllers.produto_encontra_controller import ProdutoEncontraController

def produto_encontra_constructor():
    produto_encontra_view = ProdutoEncontraView()
    produto_encontra_controller = ProdutoEncontraController()

    info_produto_busca = produto_encontra_view.encontra_produto_view()
    response = produto_encontra_controller.encontra(info_produto_busca)

    if response["success"]:
        produto_encontra_view.encontra_produto_sucesso(response["message"])
    else:
        produto_encontra_view.encontra_produto_falha(response["error"])

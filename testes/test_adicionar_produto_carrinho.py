import time
import pytest
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCt01:
    def test01_adicionar_produtos(self):
        #instancia objetos
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        #Faz login
        login_page.fazer_login("standard_user","secret_sauce")

        #Adicionando produtos ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        #acessa o carrinho
        home_page.acessar_carrinho()

        #verifica se o produto foi adicionado ao carrinho
        carrinho_page.verificar_se_item_existe_no_carrinho("Sauce Labs Backpack")

        #aperta o botao continuar comprando
        carrinho_page.clicar_continuar_comprando()

        #adiciona outro produto ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Bike Light")

        #acessa o carrinho
        home_page.acessar_carrinho()

        #verifica se ambos os produtos estao no carrinho
        carrinho_page.verificar_se_item_existe_no_carrinho("Sauce Labs Backpack")
        carrinho_page.verificar_se_item_existe_no_carrinho("Sauce Labs Bike Light")




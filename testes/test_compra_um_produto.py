import pytest
import conftest
from selenium.webdriver.common.by import By

from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCt02:
    def test02_compra_produtos(self):
        # instancia objetos
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adiciona produto ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # Acessa o carrinho
        home_page.acessar_carrinho()

        # Verifica se o produto foi adicionado ao carrinho
        carrinho_page.verificar_se_item_existe_no_carrinho("Sauce Labs Backpack")

        # clica no botão checkout
        carrinho_page.clicar_botao_checkout()

        # preenche os dados para continuar a compra e aperta o botao continue
        carrinho_page.preencher_campos_e_submter("Alisson","Macedo","09250210")


        #pressiona o botao de finalizar a compra
        carrinho_page.finalizar_compra()

        # # verifica se a compra foi efetuada
        carrinho_page.verificar_se_compra_foi_efetuada()
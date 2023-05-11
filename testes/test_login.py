import time
import pytest
import conftest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCt03:
    def test03_login(self):
        #instancia objetos
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()

        #Faz login
        login_page.fazer_login("standard_user","secret_sauce")

        #Verifica se o login foi feito com sucesso
        home_page.verificar_login_com_sucesso()

        time.sleep(3)


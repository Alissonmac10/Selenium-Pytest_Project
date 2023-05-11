import time
import pytest
import conftest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCt03:
    def test03_login_invalido(self):
        # instancia objetos
        driver = conftest.driver
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login("standard_user", "senhaInvalida")

        #Verifica mensagem de erro
        login_page.verifica_login_invalido()

        time.sleep(3)


from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.loginbutton_field = (By.ID, "login-button")
        self.error_login = (By.XPATH,'//h3[@data-test="error" and text()="Epic sadface: Username and password do not match any user in this service"]')
    def fazer_login(self,usuario,senha):

        self.escrever(self.username_field,usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.loginbutton_field)

    def verifica_login_invalido(self):
        self.verificar_se_elemento_existe(self.error_login)




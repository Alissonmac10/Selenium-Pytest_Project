
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest


class BasePage:

    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self,locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator,text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self,locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}'não foi encontrado na tela"

    def pegar_texto_elemento(self,locator):
        self.esperar_elemento_aparecer(locator)
        self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(*locator))

    def verificar_elemento_existe(self,locator):

        assert self.encontrar_elemento(locator), f"elemento '{locator}' não existe"

    def verificar_nao_elemento_existe(self, locator):

        assert len(self.encontrar_elementos(locator))==0, f"elemento '{locator}' existe"

    def clicar_duas_vezes(self, locator):

        element = self.esperar_elemento_aparecer(locator)

        ActionChains(self.driver).double_click(element).perform()

    def clicar_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)

        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator,key):

        elem = self.esperar_elemento_aparecer(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)
        elif key == "ESPACO":
            elem.send_keys(Keys.SPACE)

        ## REPETIR PARA ADICIONAR OUTRAS TECLAS








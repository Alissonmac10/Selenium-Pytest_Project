from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage



class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, '//div[@class="inventory_item_name" and text()="{}"]')
        self.botao_continuar_comprando = (By.XPATH,'//*[@class="btn btn_secondary back btn_medium" and text()="Continue Shopping"]')
        self.botao_checkout = (By.ID, 'checkout')
        self.nome_field = (By.ID, "first-name")
        self.sobrenome_field = (By.ID, "last-name")
        self.CEP_field = (By.ID, "postal-code")


        self.botao_finalizar_compra=(By.ID,"finish")
        self.mensagem_finalizacao_compra = (By.XPATH,'//h2[@class="complete-header" and text()="Thank you for your order!"]')
        self.botao_continue = (By.ID,"continue")


    def verificar_se_item_existe_no_carrinho(self,nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)

    def clicar_botao_checkout(self):
        self.clicar(self.botao_checkout)

    def preencher_campos_e_submter(self,nome,sobrenome,cep):
        self.escrever(self.nome_field,nome)
        self.escrever(self.sobrenome_field,sobrenome)
        self.escrever(self.CEP_field,cep)
        self.clicar(self.botao_continue)


    def finalizar_compra(self):
        self.clicar(self.botao_finalizar_compra)

    def verificar_se_compra_foi_efetuada(self):
        self.verificar_se_elemento_existe(self.mensagem_finalizacao_compra)






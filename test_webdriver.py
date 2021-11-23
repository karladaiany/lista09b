import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebDriver():
    def setup_method(self, method):
        self.driver = webdriver.Chrome('drivers/chrome/96/chromedriver.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_webdriver(self):
        self.driver.get("https://www.temporary-mail.net/")
        self.driver.set_window_size(945, 999)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-random").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
        self.vars["email"] = self.driver.find_element(By.CSS_SELECTOR, ".form-control").get_attribute("value")
        print("{}".format(self.vars["email"]))
        self.driver.get("https://iterasys.com.br")
        self.driver.find_element(By.LINK_TEXT, "Cadastro").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Não é Aluno? Matricule-se já!"
        self.driver.find_element(By.ID, "nome").send_keys("Karla Teste")
        self.driver.find_element(By.ID, "telefone").send_keys("(45) 99999-9999")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
        self.driver.find_element(By.ID, "senha").send_keys("pwd123")
        self.driver.find_element(By.ID, "e-captcha").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "btn_cadastro").click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").text == "Cadastro Realizado com sucesso."
        self.driver.get("https://www.temporary-mail.net/")
        self.driver.set_window_size(945, 999)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Confirme seu cadastro").click()
        self.driver.find_element(By.LINK_TEXT, "Confirmar cadastro").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h4").text == "Confirmação concluída!"
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
        self.driver.find_element(By.ID, "senha").send_keys("pwd123")
        self.driver.find_element(By.ID, "btn_login").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Configurações do Perfil"
        self.driver.find_element(By.CSS_SELECTOR, ".caret").click()
        self.driver.find_element(By.LINK_TEXT, "Sair").click()
        time.sleep(3)


# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCadastro():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cadastro(self):
    self.driver.get("https://temp-mail.org/pt/")
    self.driver.set_window_size(945, 999)
    self.driver.find_element(By.ID, "click-to-delete").click()
    time.sleep(10)
    self.driver.find_element(By.ID, "mail").click()
    self.vars["email"] = self.driver.find_element(By.ID, "mail").get_attribute("value")
    print("{}".format(self.vars["email"]))
    self.driver.get("https://iterasys.com.br")
    self.driver.find_element(By.LINK_TEXT, "Cadastro").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == " Não é Aluno? Matricule-se já!"
    self.driver.find_element(By.ID, "nome").send_keys("Karla Teste")
    self.driver.find_element(By.ID, "telefone").send_keys("(45) 99999-9999")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys(self.vars["email"])
    self.driver.find_element(By.ID, "senha").send_keys("pwd123")
    self.driver.find_element(By.ID, "e-captcha").click()
    time.sleep(10)
    self.driver.find_element(By.ID, "btn_cadastro").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").text == " Cadastro Realizado com sucesso."
  
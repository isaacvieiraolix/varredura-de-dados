import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os


drive = webdriver.Chrome()
time.sleep(10)
drive.get("https://www.mercadolivre.com.br/")
time.sleep(300)

PRODUTOS = drive.find_elements(By.XPATH, "//a[contains(@class,'dynamic-access-card-item__item-title')]")
time.sleep(10)
#preço
PRECOS = drive.find_elements(By.XPATH, "//div[contains(@class,'dynamic-access-card-item__price')]")

time.sleep(10)
for produto, preco in zip(PRODUTOS, PRECOS):
  with open("produtos.csv", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{produto.text};{preco.text}{os.linesep}")
    input("")

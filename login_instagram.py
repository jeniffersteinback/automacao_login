from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

def test_login_instagram(): 
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    usuario_input = driver.find_element(By.NAME,"username")
    senha_input = driver.find_element(By.NAME,"password")

    usuario_input.send_keys("docente.kauan")
    senha_input.send_keys("@testesenac12345")
    senha_input.send_keys(Keys.RETURN)

    time.sleep(5)

    if "Instagram" in driver.title:
        print("Login realizado com sucesso!")

    else:
        print("Falha no login.")

    
    input("Pressione Enter para sair...")
    driver.quit()

test_login_instagram()
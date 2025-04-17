from selenium import webdriver #Função que faz o login no Instagram
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
import time

def test_login_instagram(): 
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    usuario_input = driver.find_element(By.NAME,"username")  #Encontra o campo de usuário
    senha_input = driver.find_element(By.NAME,"password")  # Encontra o campo de senha

    usuario_input.send_keys("docente.kauan") # Digita o nome de usuario
    senha_input.send_keys("@testesenac12345") #Digita a senha
    senha_input.send_keys(Keys.RETURN) # Pressiona Enter para logar

    time.sleep(5) #Espera 5 segundos para o login processar

    if "Instagram" in driver.title: # Verifica o título da página tem "Instagram"
        print("Login realizado com sucesso!") # Mensagem se o login funcionar

    else:
        print("Falha no login.") # Mensagem se o login falhar

    time.sleep(3) 
    
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    print("Rolando a pagina lentamente...")
    start_time = time.time()
    while time.time() - start_time < 60:
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(1.5)
    print("Rolagem concluída")

    
    input("Pressione Enter para sair...") # Espera o usuário pressionar Enter
    driver.quit() # Fecha o navegador

test_login_instagram() # Chama a função para executar o login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#  Créer une variable pour déclencher le driver
# driver = webdriver.Edge(keep_alive=True)
driver = webdriver.Chrome(keep_alive=True)
# driver.get('https://www.kubii.fr/')
# driver.get('http://127.0.0.1:5500/') # Exemple sur un application en local

# # Récupération de la barre de recherche
# search_bar = driver.find_element(By.CLASS_NAME, "ui-autocomplete-input")

# search_bar.send_keys("Raspbarry pi")


# # Récupérer le bouton  pour lancer la recherche
# search_btn = driver.find_element(By.ID, "search_widget").find_element(By.TAG_NAME, "button")

# search_btn.click()


time.sleep(60*60*12)
driver.close()
print("Fin du scraping...")
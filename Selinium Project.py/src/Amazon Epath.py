from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Baby toys")
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter.tix import AUTO
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
#driver.switch_to.frame("callout")
singIn=driver.find_element(By.XPATH,"//button[@onclick='myFunction()']")
singIn.click()
#driver.switch_to.window(driver.window_handles[1])
search=driver.find_element(By.XPATH,"//p[@id='demo']")
print(search.text)
time.sleep(5)
click_me.click()
driver.switch_to.alert.dismiss()

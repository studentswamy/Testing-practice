from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from idlelib.idle_test.test_colorizer import source
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
Action=ActionChains(driver)
resizeable=driver.find_elments(by.XPATH,//)

#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")

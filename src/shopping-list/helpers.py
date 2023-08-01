import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Callable

def execute()

# df = pd.read_json('walmart-stores.json')
driver = webdriver.Chrome()
driver.get("https://homedepot.com")

sleep(7)

elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div/div[3]/div[1]/a/span/div[2]/div")
elem.click()
sleep(5)
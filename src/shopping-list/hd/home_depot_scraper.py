from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import Callable, List


class HomeDepotScraper:
    def __init__(self, items, zipcode, town):
        self._items = items
        self._zipcode = zipcode
        self._town = town
        self._driver = webdriver.Chrome()
        self._driver.get("https://homedepot.com")
        self._choose_store()

    def _find_ele(self, cmd):
        # return WebDriverWait(self._driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return WebDriverWait(self._driver, 60).until(EC.element_to_be_clickable(cmd))

    def _choose_store(self):
        # Click dropdown
        dropdown_xpath = "/html/body/div[3]/div[1]/div[2]/div[1]/div/div[3]/div[1]/a/span/div[2]/div"
        dropdown = self._find_ele((By.XPATH, dropdown_xpath))
        dropdown.click()

        # Click find stores button
        find_stores_xpath = "/html/body/div[10]/div[2]/div/div[2]/div/div[4]/a"
        find_stores = self._find_ele((By.XPATH,find_stores_xpath))
        find_stores.click()

        # Enter in desired zip code
        search_bar_xpath = "/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/input"
        search_bar = self._find_ele((By.XPATH, search_bar_xpath))
        search_bar.send_keys(self._zipcode, Keys.RETURN)

        # Select the given store
        WebDriverWait(self._driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".localization__button--select")))
        ids = self._driver.find_elements(By.XPATH, "//*[@data-storeinfo]")
        target_button = None
        for ii in ids:
            print(ii.get_attribute('data-storeinfo'))    # id name as string
            if (self._town in ii.get_attribute("data-storeinfo")):
                target_button = ii
                break
        ii.click()

x = HomeDepotScraper([], "13126", "")

from pathlib import Path

from drivers import Browser
from drivers import constants as C
from drivers import BrowserFirefox
from drivers import BrowserChrome
from drivers import BrowserEdge
from errors import NotSupportedBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import pandas as pd
import numpy as np

def driver_init(browser_web:str = "firefox") -> WebDriver:
    
    driver_browser = Browser()
    # Local Variables
    browser: BrowserFirefox | BrowserChrome | BrowserEdge
    
    match browser_web:
        
        case "firefox":
            browser = BrowserFirefox(driver_browser, C.FIREFOX_DRIVER_WINDOWS)
        case "chrome":
            browser = BrowserChrome(C.CHROME_DRIVER_WINDOWS)
        case "edge":
            browser = BrowserEdge(C.FIREFOX_DRIVER_WINDOWS)
        case _:
            raise NotSupportedBrowser(f"Browser not supported: {browser_web}")
            
    driver = browser.driver
    return driver


def get_code_products(path:Path) -> pd.Series:
    # TODO: To generalize the function
    
    data = pd.read_excel(path)
    # Evaluate the products have no image.
    products_no_images = data.loc[data["Imagen"].isnull()]
    code_products_no_images = products_no_images["Referencia Interna"]
    return code_products_no_images


def get_product_image(driver: WebDriver, url, list_products: pd.Series = None):
    
    # First Page
    driver.get(url)
    
    WebDriverWait(driver, 60).until( #* Wait for an element inside the DOM
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/h3[1]/a"))
            )
    
    page_image = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/h3[1]/a")
    next_page = page_image.get_attribute("href")
    
    # Second Page
    driver.get(next_page)
    
    WebDriverWait(driver, 60).until( #* Wait for an element inside the DOM
                EC.visibility_of_element_located((By.CLASS_NAME, "item_name"))
            )
    # time.sleep(10)
    driver.get_full_page_screenshot_as_file((C.BASE_DIR/"qr.png").__str__())
    
    image = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/section/div/ol/li[1]/div/img")
    
    return image.get_attribute("src")

def main():
    driver = driver_init()
    url = "https://www.automaq.pe/search?q=277"
    
    print(get_product_image(driver, url))

    
    

if __name__ == "__main__":
    get_code_products(Path("E:\PROJECTS\web_scrapper_mennekes\data\data.xlsx"))
    main()
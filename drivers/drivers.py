from pathlib import Path
from selenium import webdriver
# from errors import NotSupportedSO
from .constants import FIREFOX_DRIVER_WINDOWS
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options


class Browser():
        def __init__(self, headless:bool = True):
        # Local Variables
            
            # Setting Options
            self.options = Options()
            if headless: self.options.headless = True # Headless Mode
            self.options.add_argument("--window-size=1366x768") # Window Size
            self.options.add_argument("--disable-gpu") # Disable GPU
            self.options.add_argument("--disable-extensions") # Disable Extensions        

        def _get_options(self):
            return self.options
        
        def __str__(self) -> str:
            return ""

        def __repr__(self) -> str:
            return f"<{self.__class__.__name__}>"
    

class BrowserFirefox(): 
    
    def __init__(self, _class,  driver_path:Path, driver_so:str = "win"):
        # super().__init__(headless)
        
        self.options: Options = _class._get_options()
        
        match driver_so:
            case "win":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case "linux":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case _:
                # raise NotSupportedSO(f"SO not supported: {driver_so}")
                ...
        
        # Driver
        self.driver = webdriver.Firefox(service=self.__driver, options=self.options)

    def __str__(self) -> str:
        return f"{self.__driver}"

# TODO: Add Chrome Functionality
class BrowserChrome(): 
    
    def __init__(self, driver_path,  driver_so: str = "win", headless: bool = True):
        # super().__init__(driver_path, driver_so, headless)
        
        match driver_so:
            case "win":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case "linux":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case _:
                # raise NotSupportedSO(f"SO not supported: {driver_so}")
                ...
        
        self.driver = webdriver.Chrome(service=self.__driver, options=self.__options)

# TODO: Add Edge Functionality
class BrowserEdge(): 

    def __init__(self, driver_path, driver_so: str = "win", headless: bool = True):
        # super().__init__(driver_path, driver_so, headless)
        
        match driver_so:
            case "win":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case "linux":
                self.__driver = Service(driver_path.__str__())
                # Driver Path
                self.__driver_path = driver_path
            case _:
                # raise NotSupportedSO(f"SO not supported: {driver_so}")
                ...
        
        self.driver = webdriver.Edge(service=super().__driver, options=self.__options)
        


if __name__ == "__main__":
    browser = Browser()
    driver = BrowserFirefox(browser, driver_path=FIREFOX_DRIVER_WINDOWS)
    driver.driver.get("https://www.google.com")
    print(driver.driver.title)
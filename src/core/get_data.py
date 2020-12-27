from src.lib.webdriver import set_selenium
from bs4 import BeautifulSoup

driver = set_selenium()


def get_data(url: str) -> None:
    driver.get(url)
    print(driver.current_url)
    driver.close()

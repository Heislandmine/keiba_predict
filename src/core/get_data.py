from src.lib.webdriver import set_selenium
from bs4 import BeautifulSoup

driver = set_selenium()

base_race_url: str = ""


def get_race_urls():
    pass


def get_race_data(url: str):
    pass


def get_data(url: str) -> None:
    driver.get(url)
    print(driver.current_url)
    driver.close()

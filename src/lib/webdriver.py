from selenium import webdriver
from bs4 import BeautifulSoup


class Driver:
    def __init__(self):
        self.driver: webdriver = self._set_selenium()

    def get_html(self, path: str) -> BeautifulSoup:
        self.driver.get(path)
        source = self.driver.page_source.encode("utf-8")
        html = BeautifulSoup(source, "html.parser")

        return html

    def _set_selenium(self) -> webdriver:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver: webdriver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=options.to_capabilities(),
            options=options,
        )

        return driver

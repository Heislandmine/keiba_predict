from selenium import webdriver


def set_selenium() -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver: webdriver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=options.to_capabilities(),
        options=options,
    )

    return driver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Basepage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def click_when_ready(self, timeout: int, locator: str) -> None:
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)),
            f'Element: "{locator}" not yet clickable after {timeout} seconds')
        ActionChains(self.driver).move_to_element(element).click(element).perform()

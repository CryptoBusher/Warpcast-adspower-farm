from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from loguru import logger


class WarpcastCustomException(Exception):
    pass


class CustomWebDriver(webdriver.Chrome):
    def find_element(self, by=By.ID, value=None):
        try:
            return super().find_element(by=by, value=value)
        except NoSuchElementException as primary_exception:
            logger.debug('Failed to find element, checking Warpcast exceptions')
            if self.dodge_error_retrieving_data():
                return super().find_element(by=by, value=value)

            raise primary_exception

    def dodge_error_retrieving_data(self):
        try:
            super().find_element(By.XPATH, '//div[text()="Error retrieving data. Please try again."]')
            logger.debug('Error retrieving data exception found, navigating to warpcast homepage via direct link')
            self.get('https://warpcast.com/')
            return True
        except NoSuchElementException:
            return False

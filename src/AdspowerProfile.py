from random import randint, uniform
from time import sleep
from sys import stderr
import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger

from data.config import config


class AdspowerProfile:
    API_ROOT = 'http://local.adspower.com:50325'

    def __init__(self, profile_name: str, profile_id: str):
        self.profile_name = profile_name
        self.profile_id = profile_id

        self.driver = None
        self.action_chain = None
        self.wait = None
        self.profile_was_running = None

        self.__init_profile_logs()

    def __init_profile_logs(self):
        logger.debug('__init_profile_logs: entered method')
        with open('data/profile_logs.json') as file:
            profile_logs = json.load(file)

        if self.profile_name not in profile_logs:
            profile_logs[self.profile_name] = {}

        if "mandatory_users_subscribes" not in profile_logs[self.profile_name]:
            profile_logs[self.profile_name]["mandatory_users_subscribes"] = []

        if "mandatory_channels_subscribes" not in profile_logs[self.profile_name]:
            profile_logs[self.profile_name]["mandatory_channels_subscribes"] = []

        if "wallet_connected" not in profile_logs[self.profile_name]:
            profile_logs[self.profile_name]["wallet_connected"] = False

        with open("data/profile_logs.json", "w") as file:
            json.dump(profile_logs, file, indent=4)

    def __init_webdriver(self, driver_path: str, debug_address: str):
        chrome_driver = driver_path
        chrome_options = Options()
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"

        chrome_options.add_experimental_option("debuggerAddress", debug_address)
        driver = webdriver.Chrome(chrome_driver, options=chrome_options, desired_capabilities=caps)
        driver.implicitly_wait = config['element_wait_sec']
        self.driver = driver
        self.action_chain = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, config['element_wait_sec'])

    @staticmethod
    def random_activity_sleep():
        logger.debug('random_activity_sleep: sleeping')
        sleep(randint(config["delays"]["min_activity_sec"], config["delays"]["max_activity_sec"]))
        logger.debug('random_activity_sleep: finished sleeping')

    @staticmethod
    def random_subactivity_sleep():
        logger.debug('random_subactivity_sleep: sleeping')
        sleep(randint(config["delays"]["min_subactivity_sec"], config["delays"]["max_subactivity_sec"]))
        logger.debug('random_subactivity_sleep: finished sleeping')

    def human_hover(self, element, click=False):
        logger.debug('human_hover: entered method')
        size = element.size

        width_deviation_pixels = randint(1, int(size["width"] * config["max_click_width_deviation"]))
        height_deviation_pixels = randint(1, int(size["height"] * config["max_click_height_deviation"]))

        positive_width_deviation = randint(0, 1)
        positive_height_deviation = randint(0, 1)

        x = width_deviation_pixels if positive_width_deviation else -width_deviation_pixels
        y = height_deviation_pixels if positive_height_deviation else -height_deviation_pixels

        if click:
            logger.debug(f'human_hover: hover + clicking "{element.text}"')
            self.action_chain.move_to_element_with_offset(element, x, y).perform()
            sleep(uniform(0.5, 2))
            self.action_chain.click().perform()
        else:
            logger.debug(f'human_hover: hover only "{element.text}"')
            self.action_chain.move_to_element_with_offset(element, x, y).perform()

    def human_scroll(self):
        logger.debug('human_scroll: entered method')
        ticks_per_scroll = randint(config['min_ticks_per_scroll'], config['max_ticks_per_scroll'])
        logger.debug(f'human_scroll: {ticks_per_scroll} ticks_per_scroll')
        for tick in range(ticks_per_scroll):
            sleep(uniform(config["min_delay_between_scroll_ticks_sec"], config["max_delay_between_scroll_ticks_sec"]))
            self.driver.execute_script(f"window.scrollBy(0, {config['pixels_per_scroll_tick']});")

    def human_type(self, text: str):
        logger.debug('human_type: entered method')
        for char in text:
            sleep(uniform(config["delays"]["min_typing_sec"], config["delays"]["max_typing_sec"]))
            self.driver.switch_to.active_element.send_keys(char)

    def open_profile(self, headless: bool = False):
        url = self.API_ROOT + '/api/v1/browser/active'
        params = {
            "user_id": self.profile_id,
        }

        is_active_response = requests.get(url, params=params).json()
        if is_active_response["code"] != 0:
            raise Exception('Failed to check profile open status')

        if is_active_response['data']['status'] == 'Active':
            self.profile_was_running = True
            if not config["farm_running_profiles"]:
                raise Exception('Profile is active')

            self.__init_webdriver(is_active_response["data"]["webdriver"], is_active_response["data"]["ws"]["selenium"])

        else:
            self.profile_was_running = False
            url = self.API_ROOT + '/api/v1/browser/start'
            params = {
                "user_id": self.profile_id,
                "open_tabs": "0",
                "ip_tab": "0",
                "headless": "1" if headless else "0",
            }

            start_response = requests.get(url, params=params).json()
            if start_response["code"] != 0:
                raise Exception(f'Failed to open profile, server response: {start_response}')

            self.__init_webdriver(start_response["data"]["webdriver"], start_response["data"]["ws"]["selenium"])

    def close_profile(self):
        url_check_status = self.API_ROOT + '/api/v1/browser/active' + f'?user_id={self.profile_id}'
        url_close_profile = self.API_ROOT + '/api/v1/browser/stop' + f'?user_id={self.profile_id}'

        status_response = requests.get(url_check_status).json()
        if status_response['data']['status'] == 'Inactive':
            self.driver = None
            self.action_chain = None
            return

        close_response = requests.get(url_close_profile).json()
        if close_response["code"] != 0:
            raise Exception('Failed to close profile')

        self.driver = None

    def switch_to_tab(self, url_includes_text: str):
        logger.debug('__switch_to_tab: entered method')
        logger.debug(f'__switch_to_tab: looking for tab that includes "{url_includes_text}"')
        for tab in self.driver.window_handles:
            try:
                self.driver.switch_to.window(tab)
                if url_includes_text in self.driver.current_url:
                    logger.debug(f'__switch_to_tab: switched to window "{self.driver.current_url}"')
                    return
            except:
                pass

        raise Exception(f'Failed to find tab that includes {url_includes_text} in url')

    def wait_for_new_tab(self, init_tabs):
        logger.debug('__wait_for_new_tab: entered method')
        for i in range(config["element_wait_sec"]):
            if list(set(self.driver.window_handles) - set(init_tabs)):
                logger.debug('__wait_for_new_tab: found new tab')
                return
            else:
                sleep(1)

        raise Exception('Failed to locate new tab or extension window')

    def close_all_other_tabs(self):
        initial_tab = self.driver.current_window_handle
        tabs_to_close = self.driver.window_handles
        tabs_to_close.remove(initial_tab)

        for tab in tabs_to_close:
            self.driver.switch_to.window(tab)
            self.driver.close()

        self.driver.switch_to.window(initial_tab)
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import logging
import os

def start_driver():
    LOGGER.setLevel(logging.WARNING)
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    os.environ['WDM_LOG'] = "false"
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized','--log-level=3'] # '--incognito'
    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.add_experimental_option('prefs', {
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)
    wait = WebDriverWait(driver=driver,
                         timeout=10,
                         poll_frequency=1,
                         ignored_exceptions=[
                             NoSuchElementException,
                             ElementNotVisibleException,
                             ElementNotSelectableException
                         ])
    return driver, wait

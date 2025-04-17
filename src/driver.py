import os

from selenium import webdriver

download_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def setup_driver():
    edge_prefs = {
        'download.neverAsk.saveToDisk': 'application/xml, text/anytext, text/plaintext',
        'download.default_directory': str(download_dir),
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'disable-popup-blocking': True,
        'safebrowsing.enabled': False,
        'download_restrictions': 0,
    }

    options = webdriver.EdgeOptions()
    options.add_argument('--safebrowsing-disable-download-protection')
    options.add_argument('--headless=new')
    options.add_experimental_option('prefs', edge_prefs)

    driver = webdriver.Edge(options=options)
    return driver


def quit_driver(driver):
    driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils import *
from src.log_config import logger


def scrapy_nif(driver, file):
    info_list = []
    my_nifs = nifs(file)
    quantity_nifs = len(my_nifs)
    logger.info(f'Found {quantity_nifs} NIFs')
    logger.info('Processing NIFs...')
    for i, nif in enumerate(my_nifs):
        search_nif(driver, nif)

        details = {}
        for field in details_fields:
            details[field] = extract_info(driver, field)

        bt_conta = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Contas-tab'))
        )
        driver.execute_script('arguments[0].scrollIntoView(true);', bt_conta)
        driver.execute_script('arguments[0].click();', bt_conta)

        accounts = {}
        for field in account_fields:
            accounts[field] = extract_info(driver, field)

        info_dict = {**details, **accounts}
        info_list.append(info_dict)

        driver.get(
            'https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600'
        )
        logger.info(f'Processed NIF {i + 1} of {quantity_nifs}')
    logger.info('All NIFs processed')
    logger.info('=== END PROCESSING ===')
    return info_list

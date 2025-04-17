import time

import pandas as pd

from src.defines import *
from src.driver import quit_driver, setup_driver
from src.login import login
from src.scrapy_nif import scrapy_nif
from src.utils import delete_file, download_nifs, read_xlsx
from src.log_config import logger


def main():
    driver = setup_driver()
    logger.info('=== START PROCESSING ===')
    login(driver, email, password)
    download_nifs(driver)
    read_xlsx(INPUT_FILE)
    delete_file(INPUT_FILE)
    info = scrapy_nif(driver, 'nif_saft.txt')

    quit_driver(driver)
    logger.info('Driver closed')

    df = pd.DataFrame(info)
    process_date = time.strftime('%d-%m-%Y')
    xlsx_name = f'backup-saft-{process_date}.xlsx'
    df.to_excel(xlsx_name, index=False)
    logger.info(f'File {xlsx_name} created')

if __name__ == '__main__':
    main()
    logger.info('=== END PROCESSING ===')
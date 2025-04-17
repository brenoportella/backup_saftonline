import os
import time

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.log_config import logger
from src. defines import TIME_SLEEP, TIME_WAIT, DOWNLOAD_TIME

def extract_info(driver, field_name):
    try:
        field = WebDriverWait(driver, TIME_WAIT).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field_value = field.get_attribute('value')
    except NoSuchElementException:
        field_value = 'N/A'

    return field_value


def download_nifs(driver):
    download_bt = WebDriverWait(driver, TIME_WAIT).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, 'img-responsive.center-block')
        )
    )
    download_bt.click()
    time.sleep(DOWNLOAD_TIME)
    logger.info('Download completed')


def read_xlsx(file):
    df = pd.read_excel(file, skiprows=1, usecols=[0])
    df.to_csv('nif_saft.txt', sep='\t', index=False)
    logger.info('File converted to txt')


def delete_file(file):
    time.sleep(TIME_SLEEP)
    os.remove(file)
    logger.info(f'File {file} deleted')


def nifs(file):
    with open(file, 'r') as txt:
        nifs = [line.strip() for line in txt.readlines()]
    logger.info(f'File {file} read')
    return nifs

def search_nif(driver, nif):
    field_filter = WebDriverWait(driver, TIME_WAIT).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'mvc-grid-value'))
    )
    field_filter.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    field_filter.send_keys(nif)
    field_filter.send_keys(Keys.ENTER)
    bt_details = WebDriverWait(driver, TIME_WAIT).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'pe-7s-look'))
    )
    bt_details.click()
    logger.info(f'Searching for NIF: {nif}')


account_fields = [
    'Empresa.API_UsernameAT',
    'Empresa.API_PasswordAT',
    'Empresa.API_UsernameSS',
    'Empresa.API_PasswordSS',
    'Empresa.API_UsernameVIACTT',
    'Empresa.API_PasswordVIACTT',
    'Empresa.API_UsernameIAPMEI',
    'Empresa.API_PasswordIAPMEI',
    'Empresa.API_UsernameRU',
    'Empresa.API_PasswordRU',
    'Empresa.API_UsernameIEFP',
    'Empresa.API_PasswordIEFP',
    'Empresa.API_UsernameB2020',
    'Empresa.API_PasswordB2020',
    'Empresa.API_UsernameINE',
    'Empresa.API_PasswordINE',
    'Empresa.API_UsernameSILIAMB',
    'Empresa.API_PasswordSILIAMB',
    'Empresa.API_UsernameLivroRec',
    'Empresa.API_PasswordLivroRec',
    'Empresa.API_UsernameACT',
    'Empresa.API_PasswordACT',
]

details_fields = [
    'Empresa.Emp_NIF',
    'Empresa.Emp_Tag',
    'Empresa.Emp_Empresa',
    'Empresa.Emp_CAE',
    'Empresa.Emp_Morada',
    'Empresa.InfoGerentes',
    'Empresa.Emp_CodPostal',
    'Empresa.Emp_CodPostalLoc',
    'Empresa.InfoFreguesia',
    'Empresa.InfoConcelho',
    'Empresa.InfoDistrito',
    'Empresa.InfoDataConstituicao',
    'Empresa.InfoDataInicioAtividade',
    'Empresa.InfoReparticaoFinancas',
    'Empresa.Emp_Email',
    'Empresa.Emp_Telefone',
    'Empresa.Emp_Telemovel',
    'Empresa.Emp_EmailG',
    'Empresa.Emp_GestorNome',
    'Empresa.Emp_CertidaoPCodigo',
    'Empresa.Emp_CertidaoPValidade',
    'Empresa.Emp_TipoContabilidade',
    'Empresa.Emp_TipoIVA',
    'ContabilistaCertificadoIVA',
    'Empresa.Emp_RCBE',
]

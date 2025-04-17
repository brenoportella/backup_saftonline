from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.log_config import logger
from src.driver import quit_driver
from src.defines import TIME_WAIT
import sys

def login(driver, email, password):
    try:
        driver.get(
            'https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600'
        )

        WebDriverWait(driver, TIME_WAIT).until(
            EC.visibility_of_element_located((By.NAME, 'Email'))
        )

        field_email = driver.find_element(By.NAME, 'Email')
        field_email.send_keys(email)

        field_password = driver.find_element(By.NAME, 'Senha')
        field_password.send_keys(password)

        bt_login = driver.find_element(By.CLASS_NAME, 'btn-default')
        bt_login.click()

        WebDriverWait(driver, TIME_WAIT).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'img-responsive.center-block')
            )
        )
        logger.info('Login successful')

    except TimeoutException:
        logger.error('Login failed: Timeout waiting for element. Check your credentials or page structure.')
        quit_driver(driver)
        sys.exit(1)

    except NoSuchElementException:
        logger.error('Login failed: Element not found on page.')
        quit_driver(driver)
        sys.exit(1)
        
    except Exception as e:
        logger.error(f'Login failed with unexpected error: {str(e)}')
        quit_driver(driver)
        sys.exit(1)
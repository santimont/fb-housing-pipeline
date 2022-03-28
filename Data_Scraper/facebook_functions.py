from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


def init_driver(file_path):
    driver = webdriver.Chrome(file_path)
    driver.wait = WebDriverWait(driver, 10)
    return driver


def go_to_website(driver, website):
    driver.get(website)


def login_to_fb(driver, credentials):
    try:
        email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'email')))
        email_input.clear()
        time.sleep(1)
        email_input.send_keys(credentials.get('email'))

        password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'pass')))
        password_input.clear()
        time.sleep(1)
        password_input.send_keys(credentials.get('password'))

        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'login')))
        time.sleep(2)
        login_button.click()
    except (TimeoutException, NoSuchElementException):
       raise ValueError("Logging In Failed")

def close_window(driver):
    driver.close()

def quit_connection(driver):
    driver.quit()



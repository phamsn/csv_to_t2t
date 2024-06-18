#!/usr/bin/python3

import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

T2T_URL = "https://app.time2track.com"
USER_ELEM_ID = "user_session_login"
PASS_ELEM_ID = "user_session_password"
LOGIN_BTN_NAME = "commit"
USER = "phamsn@vt.edu"

if __name__ == "__main__":

    PASS = getpass("T2T Password: ")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 	
    browser.maximize_window()

    # logging in
    browser.get(f"{T2T_URL}/login")

    user_field = browser.find_element(By.ID, USER_ELEM_ID)
    user_field.send_keys(USER)

    pass_field = browser.find_element(By.ID, PASS_ELEM_ID)
    pass_field.send_keys(PASS)

    login_btn = browser.find_element(By.NAME, LOGIN_BTN_NAME)
    login_btn.click()


    while(True):
        time.sleep(5)
        pass



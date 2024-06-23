#!/usr/bin/python3

import time
import argparse
import csv
import math
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

T2T_URL = "https://app.time2track.com"
USER_ELEM_ID = "user_session_login"
PASS_ELEM_ID = "user_session_password"
LOGIN_BTN_NAME = "commit"
ACTIVITY_DATE_ID = "activity_date"
ACTIVITY_SETTING_ID = "activity_setting"
ACTIVITY_TYPE_ID = "activity_type"
ACTIVITY_CLIENT_ID = "client"
ACTIVITY_HOURS_ID = "activity_time_spent"
ACTIVITY_TAGS_ID = "//input[contains(@placeholder,'select or add tags')]"
ACTIVITY_ASSESSMENT_ID = "activity_assessment_name"

ADD_ANOTHER_NAME = "save_and_add"

CSV_DICT = {
    "date":                 [ACTIVITY_DATE_ID,          By.ID],
    "treatment_setting":    [ACTIVITY_SETTING_ID,       By.ID],
    "activity_type":        [ACTIVITY_TYPE_ID,          By.ID],
    "client":               [ACTIVITY_CLIENT_ID,        By.ID],
    "hours":                [ACTIVITY_HOURS_ID,         By.ID],
    "tags":                 [ACTIVITY_TAGS_ID,          By.XPATH],
    "assessments":          [ACTIVITY_ASSESSMENT_ID,    By.ID],
    }

if __name__ == "__main__":
    # handle CLI arguments
    parser = argparse.ArgumentParser(
                    prog="CSV to T2T",
                    description="This program takes field from a CSV file to add activities in Time2Track")
    parser.add_argument("filepath",
                        help = "path to csv file")
    args = parser.parse_args()

    USER = input("T2T Uusername: ")
    PASS = getpass("T2T Password: ")

    print("Logging into Time2Track account...", end = " ")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 	
    browser.maximize_window()
    browser.get(f"{T2T_URL}/login")
    browser.find_element(By.ID, USER_ELEM_ID).send_keys(USER)
    browser.find_element(By.ID, PASS_ELEM_ID).send_keys(PASS)
    browser.find_element(By.NAME, LOGIN_BTN_NAME).click()
    print("Done")

    print("Adding activities...")
    browser.find_element(By.LINK_TEXT, "Add a New Activity").click();

    with open(args.filepath) as csvfile:
        lines = csv.DictReader(csvfile)
        for line in lines:
            print(line, end = "\n\n")
            for colname in line.keys():
                element = browser.find_element(CSV_DICT[colname][1], CSV_DICT[colname][0])
                value = line[colname]

                if colname == "date":
                    element.clear();
                    element.send_keys(value)
                    element.send_keys(Keys.ENTER)
                elif colname == "treatment_setting":
                    Select(element).select_by_visible_text(value)
                elif colname == "activity_type":
                    browser.find_element(By.ID, "activity_type_chosen").click()
                    element.find_element(By.XPATH, f"//ul/li[text() = '{value}']").click()
                elif colname == "client":
                    element.send_keys(value)
                elif colname == "hours":
                    element.clear()
                    element.send_keys(value)
                elif colname == "tags":
                    tags = value.split(",")
                    for tag in tags:
                        element.send_keys(tag)
                        element.send_keys(Keys.ENTER)
                    element.send_keys(Keys.ENTER)
                elif colname == "assessments":
                    vals = value.split(",")
                    browser.find_element(By.XPATH, "//h2[@role = 'button']").click()

                    for i in range(math.floor(len(vals)/7) - 1):
                        time.sleep(0.5)
                        browser.find_element(By.XPATH, "//*[@id = 'assessments']/button").click()

                    tallies = browser.find_elements(By.XPATH, "//*/input[contains(@name, '[assessment_tallies_attributes]') and not(@type = 'hidden')]")
                    for i, tally in enumerate(tallies):
                        tally.clear()
                        tally.send_keys(vals[i])

            browser.find_element(By.NAME, ADD_ANOTHER_NAME).click()
    print("Done")

    while(True):
        time.sleep(5)
        pass

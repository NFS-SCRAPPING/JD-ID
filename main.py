import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import openpyxl
import pandas as pd
import numpy
import time
import json

from setting import USER,PASS,COOKIE,USER_G,PASS_G

import pyautogui

from setting import USER,PASS,PASS_G,USER_G

import undetected_chromedriver.v2 as uc

driver = uc.Chrome()

link = 'https://ulogin.jd.id/pc/new/login?ReturnUrl=%2F%2Fwww.jd.id'


def login_google():

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[2]/div[5]/div[3]/ul/li[1]')))
    element.click()

    time.sleep(3)

    time.sleep(8)

    pyautogui.write(USER_G) 

    time.sleep(5)

    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.write(PASS_G) 

    time.sleep(5)

    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.press('enter')
        
def main():
    print("run program")

    driver.get(link)

    driver.maximize_window()

    login_google()

    time.sleep(20)


if __name__ == "__main__":
   main()
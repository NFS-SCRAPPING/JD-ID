from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
import pathlib

path = pathlib.Path(__file__).parent.resolve()

from undetected_chromedriver import v2

class Bot:

    def __init__(self, user, passw,url, driver):
        self.user   = user
        self.passw  = passw
        self.url    = url
        self.driver = driver

    def login_google(self):

        link = 'https://ulogin.jd.id/pc/new/login?ReturnUrl=%2F%2Fwww.jd.id'

        self.driver.get(link)

        self.driver.set_window_size(800, 800)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[2]/div[5]/div[3]/ul/li[1]')))
        element.click()

        time.sleep(3)
        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        email.send_keys(self.user)
        time.sleep(8)

        next_e = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button')))
        next_e.click()

        time.sleep(5)

        pasw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        pasw.send_keys(self.passw)

        time.sleep(5)

    
        next_p = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button')))
        next_p.click()

        time.sleep(10)

    def flash_sale(self):

        self.driver.get(self.url)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="m_common_content"]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div[1]/div[2]/div[2]/a')))
        element.click()

        
        method = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fillOrderPanel"]/div[1]/div[2]/div[2]/div[2]/div[1]')))
        method.click()
            

        bayar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="payPanel"]/div[3]/div[1]/div[2]/a')))
        bayar.click()

        lanjutkan = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="payPanel"]/div[3]/div[2]/div[2]/div/div[3]/span/button[2]')))
        lanjutkan.click()
    


def run(email,psw,url):

    driver  = v2.Chrome()

    run = Bot(email,psw,url,driver)

    run.login_google()

    run.flash_sale()



def main():

    print("run program")
    #
    sheets_names = pd.read_excel(f'{path}/data.xlsx')

    arr = sheets_names.to_numpy()

    email = arr[0][0]
    psw   = arr[0][1]
    url   = arr[0][2]

    try:
        run(email,psw,url)
    except Exception:
        print("error")
        time.sleep(60)
    

    time.sleep(60)


if __name__ == "__main__":
   main()
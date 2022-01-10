import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from multiprocessing import Process, freeze_support
import pandas as pd
from time import sleep

em = "" # Insert your email here
pw = "" # Insert your password here
dir = "" # Insert your subscriptions.csv file directory
user_data_dir = "" # Insert your user data directory

freeze_support()
options = uc.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument(f"--user-data-dir={user_data_dir}")

driver = uc.Chrome(options=options)

subs = pd.read_csv(dir)
urls = subs["URL channel"]

def login():
    sleep(20)
    driver.find_element(By.CSS_SELECTOR, ".WpHeLc.VfPpkd-mRLv6.VfPpkd-RLmnJb").click()
    driver.find_element(By.ID, "identifierId").send_keys(em)
    driver.find_element(By.CSS_SELECTOR, ".VfPpkd-vQzf8d").click()
    sleep(2.5)
    driver.find_element(By.NAME, "password").send_keys(pw)
    driver.find_element(By.CSS_SELECTOR, ".VfPpkd-vQzf8d").click()

def main():
    for url in urls:
        driver.get(url)
        login()
        try:
            driver.find_element(By.CSS_SELECTOR, ".style-scope.ytd-subscribe-button-renderer").click()
        except:
            continue
        sleep(1)

if __name__ == '__main__':
    main()
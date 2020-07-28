from selenium import webdriver

import time
from selenium.webdriver.chrome.options import Options

"""

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"

"""

def main():
    email  = "Emailmu Borrr"
    passwd = "PasswordFB Mu Borrr"
    path = "C:/tools/chromedriver/chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

    driver  = webdriver.Chrome(path,options=options)
    driver.get("https://getzen.cash/")

    # Wait
    time.sleep(5)

    # Claim Button Click To Login
    claim_btn = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[1]/div/form/div[2]/button[2]")
    claim_btn.click()
    time.sleep(2)
    # claim_btn.click()
    print("Button Clicked")

    # Login With FB
    fb_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/a[2]")
    fb_btn.click()
    time.sleep(3)

    #Fb Form Handler
    username_form = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")
    username_form.send_keys(email)

    password_form = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")
    password_form.send_keys(passwd)

    fb_login_btn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")
    fb_login_btn.click()
    
    time.sleep(3)
    print("Login Sukses")

    #Captcha And Claim
    captcha_btn = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[1]/div/form/div[2]/div/div/div/iframe")
    captcha_btn.click()
    claim_btn.click()

if __name__ == '__main__':
    main()

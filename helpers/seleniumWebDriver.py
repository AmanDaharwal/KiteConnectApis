from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers.totpModule import fetchTotp


def launchbrowser(url):
    driver = chromedriver_path = '../resources/chromedriver.exe'

    # Create Chrome WebDriver instance
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximize the browser window
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    # Launch the URL
    driver.get(url)
    driver.implicitly_wait(10)
    print("URL >>> " + url)

    # enter usernameTxtbox and passwordTxtBox
    usernameTxtbox = driver.find_element(by=By.ID, value="userid")
    usernameTxtbox.send_keys("username")

    passwordTxtbox = driver.find_element(by=By.ID, value="password")
    passwordTxtbox.send_keys("password")

    loginBtn = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Login')]")
    loginBtn.click()

    otp = fetchTotp()
    print("Current TOTP is "+otp)

    totpTxtbox = driver.find_element(by=By.XPATH, value="//input[contains(@label,'TOTP')]")
    totpTxtbox.send_keys(otp)

    # continueBtn = driver.find_element(by=By.XPATH, value="//button[contains(text(),'Continue')]")
    # continueBtn.click()

    return driver


def getcurrenturl(driver):
    currentUrl = driver.current_url
    print("Redirected URL >>> " + currentUrl)
    return currentUrl


def quitselenium(driver):
    driver.quit()

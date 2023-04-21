from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

username = "username"
password = "password"

driver.get("https://twitter.com/login")
time.sleep(2)

username_inpt = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username_inpt.send_keys(username)
username_inpt.send_keys(Keys.ENTER)
time.sleep(2)

password_inpt = driver.find_element(By.XPATH, "//input[@name='password']")
password_inpt.send_keys(password)

password_inpt.send_keys(Keys.ENTER)
print("success")
time.sleep(2)

driver.get("https://twitter.com/username/with_replies")
time.sleep(4)

tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
print("tweets: ", len(tweets))
time.sleep(2)
for tweet in tweets:
    delete_button = tweet.find_element(By.XPATH,".//div[@data-testid='caret']")
    delete_button.click()
    print("delete")
    time.sleep(2)
    delete_option = driver.find_element(By.XPATH, "//div[@role='menuitem'][@tabindex='0']//span[text()='Excluir']")
    delete_option.click()
    time.sleep(2)
    confirm_delete = driver.find_element(By.XPATH, "//div[@data-testid='confirmationSheetConfirm']")
    confirm_delete.click()
    time.sleep(2)

driver.quit()
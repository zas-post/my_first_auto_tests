from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.ID, "book")
button.click()

browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element(By.ID,"input_value").text
y = calc(x_element)

input1 = browser.find_element(By.CLASS_NAME,'form-control')
input1.send_keys(y)

button = browser.find_element(By.XPATH,"//button[@type='submit']")
button.click()

time.sleep(5)

browser.quit()

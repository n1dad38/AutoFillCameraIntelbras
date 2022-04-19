from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_webdriver = webdriver.Chrome()
ip_default = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1650405558&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7db95652-6cab-ee4e-5b2a-2cd70f353573&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"

chrome_webdriver.get(ip_default)

element = WebDriverWait(chrome_webdriver, 10).until(
    EC.presence_of_element_located((By.ID, "i0116"))
)

field = chrome_webdriver.find_element_by_id("i0116")
field.send_keys("teste@teste.com")

button = chrome_webdriver.find_element_by_id("idSIButton9")
button.click()

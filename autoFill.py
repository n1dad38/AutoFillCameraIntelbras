from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

inp = input("IP: ")
new = input("New Ip: ")
teste = new.split('.')
ip_default = "http://" + str(inp) 
ja_preenc = input("Inicialização Já Feita? (S/N): ")
chrome_webdriver = webdriver.Chrome()

chrome_webdriver.get(ip_default)

if ja_preenc == 'n':
    element = WebDriverWait(chrome_webdriver, 10).until(
        EC.presence_of_element_located((By.NAME, "newpwd"))
    )

    field = chrome_webdriver.find_element_by_name("newpwd")
    field.send_keys("admin@1234")

    field = chrome_webdriver.find_element_by_name("newpwdcfm")
    field.send_keys("admin@1234")

    field = chrome_webdriver.find_element_by_id("devInit_bindMail")
    field.send_keys("samuel@lygs.com.br")

    field = chrome_webdriver.find_element_by_id('devInit_bindPhone')
    field.send_keys("11953330447")

    button = chrome_webdriver.find_element_by_xpath('//*[@id="device_init"]/div[3]/div/a')
    button.click()

    element = WebDriverWait(chrome_webdriver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login_permission1"]/div[2]/div[2]/label[1]/label'))
    )

    button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission1"]/div[2]/div[2]/label[1]/label')
    button.click()

    button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission1"]/div[3]/div/a')
    button.click()

    element = WebDriverWait(chrome_webdriver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login_permission3"]/div[3]/div/a'))
    )

    button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission3"]/div[3]/div/a')
    button.click()
    
element = WebDriverWait(chrome_webdriver, 10).until(
    EC.presence_of_element_located((By.ID, "login_user"))
)

field = chrome_webdriver.find_element_by_xpath('//*[@id="login_user"]')
field.send_keys("admin")

field = chrome_webdriver.find_element_by_xpath('//*[@id="login_psw"]')
field.send_keys('admin@1234')

button = chrome_webdriver.find_element_by_xpath('//*[@id="login"]/div[1]/div[1]/div[2]/form/div[6]/a')
button.click()


element = WebDriverWait(chrome_webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="custom_menu_wrap"]/ul[2]/li[2]/label'))
)

button = chrome_webdriver.find_element_by_xpath('//*[@id="custom_menu_wrap"]/ul[2]/li[2]/label')
button.click()

element = WebDriverWait(chrome_webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="custom_menu_container"]/div/ul[1]/li[3]/i'))
)

button = chrome_webdriver.find_element_by_xpath('//*[@id="custom_menu_container"]/div/ul[1]/li[3]/i')
button.click()

element = WebDriverWait(chrome_webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="page_networkConfig"]/div/div/div[1]/div[1]/label[2]/label'))
)

button = chrome_webdriver.find_element_by_xpath('//*[@id="page_networkConfig"]/div/div/div[1]/div[1]/label[2]/label')
button.click()

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[1]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[0])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[2]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[1])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[3]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[2])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[4]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[3])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[1]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[0])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[2]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[1])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[3]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(teste[2])

field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[4]')
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys(Keys.BACKSPACE)
field.send_keys('1')



button = chrome_webdriver.find_element_by_xpath('//*[@id="page_networkConfig"]/div/div/div[5]/a[2]')
button.click()

chrome_webdriver.close()

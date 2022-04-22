from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from autoFillSupp import waitByName, waitByXPath, waitById
from sheetParser import excelParser

# Enter with the first line of the excel file
firstLine = int(input("\u001b[33mA partir de qual linha? \u001b[0m"))

# Fill the path here: 
ipsList = excelParser("path", firstLine)

# Gateway handling
gateway = [ipsList[0].split('.')[0], ipsList[0].split('.')[1], ipsList[0].split('.')[2], '1']

n = int(0)

currentIp = input("\u001b[33mIP padrão das câmeras: \u001b[0m")
path = "http://" + str(currentIp) 
alreadyFilled = input("\u001b[33mInicialização Já Feita? \u001b[35m(s/n)\u001b[33m: \u001b[0m")

# Default Password
if alreadyFilled == 'n':
    defaultPasswd = str(input("\u001b[33mDigite a senha padrão a ser utilizada: \u001b[0m"))
else:
    defaultPasswd = str(input("\u001b[33mSenha para Login: \u001b[0m"))


for a in range(len(ipsList)):
    # First Access:
    if alreadyFilled == 'n':

        # Initiating
        chrome_webdriver = webdriver.Chrome()
        chrome_webdriver.get(path)

        # First Configuration
        waitByName(chrome_webdriver, "newpwd")
        
        field = chrome_webdriver.find_element_by_name("newpwd")
        field.send_keys(defaultPasswd)

        field = chrome_webdriver.find_element_by_name("newpwdcfm")
        field.send_keys(defaultPasswd)

        field = chrome_webdriver.find_element_by_id("devInit_bindMail")
        field.send_keys("samuel@lygs.com.br")

        field = chrome_webdriver.find_element_by_id('devInit_bindPhone')
        field.send_keys("11953330447")

        button = chrome_webdriver.find_element_by_xpath('//*[@id="device_init"]/div[3]/div/a')
        button.click()

        sleep(5)

        button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission1"]/div[2]/div[2]/label[1]/label')
        button.click()

        button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission1"]/div[3]/div/a')
        button.click()

        sleep(1)

        button = chrome_webdriver.find_element_by_xpath('//*[@id="login_permission3"]/div[3]/div/a')
        button.click()

        # Just testing the refresh page
        chrome_webdriver.refresh()
        

    # After first access:
    #Login Area
    waitById(chrome_webdriver, "login_user")

    #User
    chrome_webdriver.find_element_by_xpath('//*[@id="login_user"]').send_keys("admin")
    #Password
    chrome_webdriver.find_element_by_xpath('//*[@id="login_psw"]').send_keys(defaultPasswd)
    #Submit Login
    chrome_webdriver.find_element_by_xpath('//*[@id="login"]/div[1]/div[1]/div[2]/form/div[6]/a').click()

    # Navigation Area
    waitByXPath(chrome_webdriver, '//*[@id="custom_menu_wrap"]/ul[2]/li[2]/label')

    chrome_webdriver.find_element_by_xpath('//*[@id="custom_menu_wrap"]/ul[2]/li[2]/label').click()

    waitByXPath(chrome_webdriver, '//*[@id="custom_menu_container"]/div/ul[1]/li[3]/i')

    chrome_webdriver.find_element_by_xpath('//*[@id="custom_menu_container"]/div/ul[1]/li[3]/i').click()

    waitByXPath(chrome_webdriver, '//*[@id="page_networkConfig"]/div/div/div[1]/div[1]/label[2]/label')

    chrome_webdriver.find_element_by_xpath('//*[@id="page_networkConfig"]/div/div/div[1]/div[1]/label[2]/label').click()

    # IP handling:
    handledIP = [ipsList[n].split('.')[0], ipsList[n].split('.')[1], ipsList[n].split('.')[2], ipsList[n].split('.')[3]]

    # Filling IP
    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[1]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(handledIP[0])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[2]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(handledIP[1])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[3]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(handledIP[2])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_IP"]/input[4]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(handledIP[3])


    #Filling Gateway
    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[1]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(gateway[0])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[2]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(gateway[1])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[3]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(gateway[2])

    field = chrome_webdriver.find_element_by_xpath('//*[@id="NN_IPV4_DG"]/input[4]')
    for i in range(3):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys(gateway[3])

    #Clicking Apply
    chrome_webdriver.find_element_by_xpath('//*[@id="page_networkConfig"]/div/div/div[5]/a[2]').click()

    #Waiting for save
    sleep(3)

    #Closing browser
    chrome_webdriver.close()

    #If last Ip in list
    if ipsList[-1] != ipsList[n]:
        prox = input("\u001b[33mSe outra câmera plugada e pingando pressione enter.\u001b[0m")
        n += 1
    else:
        print("\u001b[32mFinalizado!\u001b[0m")

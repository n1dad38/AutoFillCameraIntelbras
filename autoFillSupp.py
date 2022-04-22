from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitByName(wd: webdriver, name: str):
    
    WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.NAME, name))
        )

def waitByXPath(wd: webdriver, xpath: str):
    
    WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

def waitById(wd: webdriver, id: str):
    
    WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.ID, id))
        )

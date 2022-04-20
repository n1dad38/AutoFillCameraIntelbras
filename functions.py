from tkinter import WORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Functions:

    def waitByName(self, wd: webdriver, name: str):
        
        WebDriverWait(wd, 10).until(
                EC.presence_of_element_located((By.NAME, name))
            )
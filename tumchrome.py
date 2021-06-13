from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd
import csv
import urllib
import socket



s = socket.socket()
print('socket created')

s.bind(('localhost', 9998))
s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with', addr, name)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    c.send(bytes(driver, 'utf-8'))
    url = f'https://https://github.com/'
    driver.get(url)
    driver.maximize_window()
    sleep(5)

    c.close()



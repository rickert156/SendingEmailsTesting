from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from data.template import subj, message
import time, csv

accounts = 'account.csv'
file_dir = 'data'

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")

rec = 'maksimnegulyaev@gmail.com'

def loginGmail(driver, login, password):
	
	login_input = driver.find_element(By.NAME, 'identifier')
	login_input.send_keys(login)
	login_input.send_keys(Keys.ENTER)
	time.sleep(2)
	password_input = driver.find_element(By.NAME, 'Passwd')
	password_input.send_keys(password)
	password_input.send_keys(Keys.ENTER)
	time.sleep(4)

def send(driver, login, number_send):
	button_new_message = driver.find_element(By.CLASS_NAME, 'T-I.T-I-KE.L3')
	button_new_message.click()
	time.sleep(2)
	recipient = driver.find_element(By.CLASS_NAME, 'agP.aFw')
	recipient.send_keys(rec)
	title = driver.find_element(By.NAME, 'subjectbox')
	title.send_keys(f'{number_send} {login} {subj}')
	body = driver.find_element(By.CLASS_NAME, 'Am.aiL.Al.editable.LW-avf.tS-tW')
	body.send_keys(message)
	button_send = driver.find_element(By.CLASS_NAME, 'T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
	button_send.click()
	time.sleep(2)
	driver.close()

with open(f'{file_dir}/{accounts}', 'r') as file:
	number_send = 0
	for account in csv.DictReader(file):
		number_send+=1
		login = account['login']
		password = account['password']
		driver = webdriver.Chrome(options=chrome_options)
		driver.maximize_window()
		driver.get('https://mail.google.com/mail/u/0/#inbox')
		loginGmail(driver, login, password)
		send(driver, login, number_send)
		print(f'[{number_send}] Отправлено с {login}')
	input('Нажмите клавишу для выхода...')


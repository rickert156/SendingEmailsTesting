from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from gmail import login, password
import time

file = 'list.txt'

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

def send():
	with open(file, 'r') as read_file:
		number_string = 0
		for domain in read_file.readlines():
			number_string+=1
			domain = domain.strip()
			email = f'vlad@{domain}'
			sendMessage(number_string, email)
		input('Нажми любую кнопку для выхода...')



def sendMessage(number_string, email):
	button_new_message = driver.find_element(By.CLASS_NAME, 'T-I.T-I-KE.L3')
	button_new_message.click()
	time.sleep(2)
	recipient = driver.find_element(By.CLASS_NAME, 'agP.aFw')
	recipient.send_keys(f'{email}')
	theme = driver.find_element(By.NAME, 'subjectbox')
	theme.send_keys(f'Redirect Test {number_string}: {email}')
	messages = driver.find_element(By.CLASS_NAME, 'Am.aiL.Al.editable.LW-avf.tS-tW')
	messages.send_keys(f'Redirect Test: {email}')
	send_button = driver.find_element(By.CLASS_NAME, 'T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
	send_button.click()
	print(f'[{number_string}] Письмо отравлено на: {email}')
	time.sleep(2)

def main():
	driver.get('https://mail.google.com/mail/u/0/')
	time.sleep(3)
	try:
		gmail_login = driver.find_element(By.TAG_NAME, 'input')
		gmail_login.send_keys(login)
		time.sleep(1)
		gmail_login.send_keys(Keys.ENTER)
		time.sleep(3)
		gmail_password = driver.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')
		gmail_password.send_keys(password)
		gmail_password.send_keys(Keys.ENTER)
		time.sleep(5)
		send()
	except Exception as ex:
		print(f'Error: {ex}')


if __name__ == '__main__':
	main()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

document = 'list.txt'
main_domain = 'digitaloctane.co'


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("start-maximized")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(f'https://{main_domain}')
time.sleep(2)

def chechDomain(num_domain, domain):
	current_url = driver.current_url
	if main_domain in current_url:print(f'[{num_domain}]Request to: {domain}')
	else:print(f'Domain {domain} not Redirect to {main_domain}\n')

def redirect(domain, num_domain):
	try:
		driver.get(f'https://{domain}')
		time.sleep(2)
	except:print(f'\n[{num_domain}]Domain {domain} not defined!')

def main():
	with open(document, 'r') as file:
		domains = file.readlines()
		num_domain = 0
		for domain in domains:
			domain = domain.strip()
			num_domain+=1
			redirect(domain, num_domain)
			chechDomain(num_domain, domain)

		input('Нажми любую кнопку для выхода...')


if __name__ == '__main__':
	main()

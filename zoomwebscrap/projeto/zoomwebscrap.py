from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument()
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://zoom.us')

login = driver.find_element_by_link_text('EFETUAR LOGIN')

login.click()

"""options= Options()
options.add_argument('user-data-dir=C:/Users/gigio/AppData/Local/Google/Chrome/User Data/Default')
chrome = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
chrome.get("https://zoom.us/profile")
#chrome.quit()"""

username = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[1]/div/input')
putusername = username.send_keys('gabriel@xxx.com.br')

userpass = driver.find_element_by_id('password')
putuserpass = userpass.send_keys('xxxxxx')

logar = driver.find_element_by_link_text('Efetuar Login')
logar.click()







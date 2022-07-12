from selenium import webdriver
pip3 install selenium
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
pip3 install webdriver-manager
cmd using pip3
username = input('PI Enter Your Facebook Username, Email or Phone No.: ')
passwd = getpass('Enter Your Facebook Password: ')
driver = webdriver.Chrome(ChromeDriverManager().install)
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver')
driver.get('https://www.facebook.com')
txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)
txtPasswd = driver.find_element_by_id('pass')
txtPasswd.send_keys(passwd)
btnLogin = driver.find_elements_by_id('u_0_b')
btnLogin.submit()
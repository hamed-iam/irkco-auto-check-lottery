from selenium import webdriver
import time
from secret import username,password;


driver = webdriver.Chrome()
driver.get('https://esale.ikco.ir/')
time.sleep(5)
loginUser = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/figure/a')
loginUser.click()
time.sleep(2)
loginCode = driver.find_element_by_xpath('//*[@id="mainIcons"]/div/div[2]/div/div/section/div/div[5]/div[2]/form/fieldset[2]/div[1]/input');
passcode = driver.find_element_by_xpath('//*[@id="passwordNew"]')
loginCode.send_keys('username');
passcode.send_keys('password')
time.sleep(2)
loginbtn = driver.find_element_by_xpath('//*[@id="LoginButton"]')
loginbtn.click();
time.sleep(2)
driver.get('https://esale.ikco.ir/#!/customer/lottery')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mainIcons"]/div/div[2]/div/div/section/div/form').get_text()
# driver.get_screenshot_as_file('testResult.png')

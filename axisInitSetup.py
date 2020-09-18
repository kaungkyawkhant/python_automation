from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import win32com.client

user = "admin"
pw = "password"
dnsIpaddress = "8.8.8.8"
txtFile = "iplist.txt"
selectIpfile = open(txtFile,'r')
selectIpfile.seek(0)
ipList = selectIpfile.readlines()
selectIpfile.close()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

temp = 1
for ip in ipList:
    link = "https://"+ ip.rstrip()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[temp])
    driver.get(link)
    print("Now accessing: " + link)
    temp += 1
    sleep(1)

    shell = win32com.client.Dispatch("WScript.Shell")  
    sleep(1) 
    shell.Sendkeys("root")  
    sleep(1)
    shell.Sendkeys("{TAB}")
    sleep(1)     
    shell.Sendkeys("password") 
    sleep(1)
    shell.Sendkeys("{ENTER}")
    sleep(5)
    #initial setup
    driver.find_element_by_xpath("//*[@id='wizardSubmitBtn']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@id='wizardSubmitBtn']").click()
    sleep(5)
    driver.find_element_by_xpath("//*[@id='orientationDoneBtn']").click()
    sleep(3)
    #click settings button
    driver.find_element_by_xpath("//*[@id='settings-toggle-up']/span").click()
    sleep(1)
    #click system button
    driver.find_element_by_xpath("//*[@id='systemMenuItem']/a/span/span").click()
    sleep(1)
    #click TCP IP button
    driver.find_element_by_xpath("//*[@id='ip']").click()
    sleep(1)
    #click DNS server button
    dnsInput = driver.find_element_by_xpath("//*[@id='AXIS-dns1Setting']")
    dnsInput.send_keys(Keys.BACKSPACE*8)
    dnsInput.send_keys(dnsIpaddress)
    sleep(1) 
    #click save button
    driver.find_element_by_xpath("//*[@id='AXIS-applyIPSettings']/button").click()
    sleep(1)
    # driver.quit()

#initial setup
#//*[@id="wizardSubmitBtn"]
#//*[@id="wizardSubmitBtn"]
#5 sec
#//*[@id="orientationDoneBtn"]

#setting
#//*[@id="settings-toggle-up"]/span
#system
#//*[@id="systemMenuItem"]/a/span/span
#TCP IP
#//*[@id='ip']
#DNS server
#//*[@id="AXIS-dns1Setting"]
#//*[@id="AXIS-applyIPSettings"]/button
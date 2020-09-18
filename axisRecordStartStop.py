from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import autoit
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import win32com.client

user = "admin"
pw = "password"
dnsIpaddress = ""
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
    #click recording button button
    driver.find_element_by_xpath("//*[@id='peripheralWrap']/div[1]/header/nav/div/div[3]/button").click()
    sleep(1)
   
    # driver.quit()

#recording
#//*[@id="peripheralWrap"]/div[1]/header/nav/div/div[3]/button
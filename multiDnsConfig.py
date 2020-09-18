from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

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
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    #enter user credentials
    username.send_keys(user)
    password.send_keys(pw)
    
    #click login button
    driver.find_element_by_xpath("//*[@id='login']/table/tbody/tr/td[2]/div/div[5]/button").click()
    sleep(1)
    #Go to configuration at top navigation
    driver.find_element_by_xpath("//*[@id='nav']/li[5]/a").click()
    sleep(1)
    #Go to Network at left navigation
    driver.find_element_by_xpath("//*[@id='menu']/div/div[3]/div[1]/span[2]").click()
    sleep(1)
    #Go to DNS text box
    dnsValue = driver.find_element_by_xpath("//*[@id='basicTcpIp']/div/div[18]/span[2]/input")
    dnsValue.clear()
    dnsValue.send_keys(dnsIpaddress)
    sleep(1)
    #click save button
    driver.find_element_by_xpath("//*[@id='basicTcpIp']/button/span[2]").click()
    sleep(1)


#//*[@id="menu"]/div/div[3]/div[1]/span[2]
#//*[@id="basicTcpIp"]/div/div[18]/span[2]/input
#//*[@id="basicTcpIp"]/button/span[2]
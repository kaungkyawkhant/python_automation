from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

user = "admin"
pw = "password"

txtFile = "iplist1.txt"

selectIpfile = open(txtFile,'r')

selectIpfile.seek(0)

ipList = selectIpfile.readlines()
selectIpfile.close()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
temp =1
for ip in ipList:
    link = "https://"+ ip.rstrip()

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[temp])
    driver.get(link)
    print("Now accessing: " + link)
    temp += 1
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

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
    #Go to Security at left navigation
    driver.find_element_by_xpath("//*[@id='menu']/div/div[2]/div[4]/span").click()
    sleep(1)
    #Go to Security Service at top navigation
    driver.find_element_by_xpath("//*[@id='ui-id-9']").click()
    sleep(1)
    #check or uncheck Enable SSH check box
    driver.find_element_by_xpath("//*[@id='enableSSH']").click()
    sleep(1)
    #check or uncheck Enable HTTP check box
    # driver.find_element_by_xpath("//*[@id='enableHTTP']").click()
    # sleep(1)
    #click save button
    driver.find_element_by_xpath("//*[@id='securityService']/button").click()
    sleep(1)

#//*[@id="menu"]/div/div[2]/div[4]/span
#//*[@id="ui-id-9"]
#//*[@id="enableSSH"]
#//*[@id="enableHTTP"]
#//*[@id="securityService"]/button
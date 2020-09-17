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

for ip in ipList:
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)

    url = "https://" + ip + "/"

    driver.get(url)

    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys(user)
    password.send_keys(pw)

    driver.find_element_by_xpath("//*[@id='login']/table/tbody/tr/td[2]/div/div[5]/button").click()

    driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[5]/a").click()
    driver.close()

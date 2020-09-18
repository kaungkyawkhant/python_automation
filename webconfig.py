from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

user = "admin"
pw = "password"

txtFile = "iplist.txt"

selectIpfile = open(txtFile,'r')

selectIpfile.seek(0)

ipList = selectIpfile.readlines()
selectIpfile.close()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

for ip in ipList:
    link = "https://"+ ip.rstrip()
    print(link)
    driver.get(link)

    #driver.execute_script('''window.open(url,"_blank");''')
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

    sleep(3)

    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys(user)
    password.send_keys(pw)
    
    driver.find_element_by_xpath("//*[@id='login']/table/tbody/tr/td[2]/div/div[5]/button").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@id='nav']/li[5]/a").click()
    sleep(3)

    #driver.close()


#//*[@id="nav"]/li[5]/a

#//*[@id="nav"]/li[5]/a, /html/body/div[2]/div/ul/li[5]/a
# wait for page to load completely 
#sleep(5)   
#driver.switch_to_frame("iframe")
#driver.find_element_by_css_selector("input[type = 'username']").send_keys(user)
#driver.find_element_by_css_selector("input[type = 'password']").send_keys(pw)
#driver.find_element_by_css_selector('Login').click()
#driver.switch_to.default_content()
#driver.close()


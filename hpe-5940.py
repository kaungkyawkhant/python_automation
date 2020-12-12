from netmiko import ConnectHandler
import sys
import time

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

dtype = 'hp_comware'
uname = 'username'
passwd = 'password'
txtFile = "hpe-dsw.txt"

selectIpfile = open(txtFile,'r')

selectIpfile.seek(0)

ipList = selectIpfile.readlines()
selectIpfile.close()

for ipaddr in ipList:
    ipaddr = ipaddr.rstrip()
    try:
        net_connect = ConnectHandler(device_type=dtype, ip=ipaddr, username=uname, password=passwd)
        time.sleep(1)
        # Get hostname of switch
        hostname = net_connect.find_prompt()
        hostname = hostname.strip('<>')
        #Get version info
        dVoutput = net_connect.send_command('display version')
        filename = hostname + '-' +ipaddr + '-' + today + ".txt"
        saveconfig=open(filename,'w+')
        print(ipaddr + " Saving version to file")
        saveconfig.write(dVoutput + "\n")
        saveconfig.close()
        #Get current config
        ddMoutput = net_connect.send_command('display device manuinfo')
        saveconfig=open(filename,'a+')
        print(ipaddr + " Saving Manuinfo to file")
        saveconfig.write(ddMoutput + "\n")
        saveconfig.close()
        #Get current config
        dCoutput = net_connect.send_command('display current')
        saveconfig=open(filename,'a+')
        print(ipaddr + " Saving current configuration to file")
        saveconfig.write(dCoutput + "\n")
        saveconfig.close()
    except:
        print(ipaddr + " is offline")
        pass

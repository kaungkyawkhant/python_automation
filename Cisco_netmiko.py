from netmiko import ConnectHandler
import getpass
import sys
import time

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

##initialising device
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }
##opening IP file
ipfile=open("iplist.txt")
print ("Script to take backup of devices, Please enter your credential")
device['username']=input("User name: ")
device['password']=getpass.getpass()

##taking backup
for line in ipfile:
 try:
     device['ip']=line.strip("\n")
     print("\n\nConnecting Device ",line)
     net_connect = ConnectHandler(**device)
     net_connect.enable()
     time.sleep(1)
     print ("Reading the hostname of switches ")
     output = net_connect.send_command('show run | inc hostname')
     time.sleep(3)
     filename=device['ip']+'-all-'+today+".txt"
     saveconfig=open(filename,'w+')
     print("Writing hostname to file")
     saveconfig.write(output + "\n")
     saveconfig.close()
     time.sleep(2)
     print ("Reading the IP Address of switches ")
     output = net_connect.send_command('sh run | i ip address 10.')
     time.sleep(3)
     filename=device['ip']+'-all-'+today+".txt"
     saveconfig=open(filename,'a+')
     print("Writing IP Address to file")
     saveconfig.write(output + "\n")
     saveconfig.close()
     time.sleep(2)
     print ("Reading the inventory of switches ")
     output = net_connect.send_command('show inventory | inc SN:')
     time.sleep(3)
     filename=device['ip']+'-all-'+today+".txt"
     saveconfig=open(filename,'a+')
     print("Writing Serial Numbers to file")
     saveconfig.write(output + "\n")
     saveconfig.close()
     time.sleep(2)
     print ("Reading the running config ")
     output = net_connect.send_command('show run')
     time.sleep(3)
     filename=device['ip']+'-all-'+today+".txt"
     saveconfig=open(filename,'a+')
     print("Writing Configuration to file")
     saveconfig.write(output)
     saveconfig.close()
     time.sleep(2)
     net_connect.disconnect()
     print ("Configuration saved to file",filename)
 except:
           print ("Access to "+device['ip']+" failed,backup did not taken")

ipfile.close()
print ("\nAll device backup completed")

from netmiko import ConnectHandler
import sys
import time

##getting system date 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

dtype = 'aruba_os'
uname = 'username'
passwd = 'password'
ipFile = "iplist.txt"
cmdFile = "aruba_cmd.txt"

selectIpfile = open(ipFile,'r')
selectIpfile.seek(0)
ipList = selectIpfile.readlines()
selectIpfile.close()

selectCmdfile = open(cmdFile,'r')
selectCmdfile.seek(0)
cmdList = selectCmdfile.readlines()
selectCmdfile.close()

for ipaddr in ipList:
    ipaddr = ipaddr.rstrip()

    try:
        net_connect = ConnectHandler(device_type=dtype, ip=ipaddr, username=uname, password=passwd)
        time.sleep(1)
        #Configure switch using cmd file

        #net_connect.send_config_from_file(cmdList)
        hostname = net_connect.find_prompt()
        hostname = hostname.rstrip('#')

        for cmd in cmdList:
            cmd = cmd.rstrip()
            cmdOutput = net_connect.send_command(cmd, expect_string=r"#")
            print("Sending command '" + cmd + "' to " + ipaddr)
            print(cmdOutput)

        filename = hostname + '-' +ipaddr + '-' + today + ".txt"
        #Get running config
        sRoutput = net_connect.send_command('show run')
        saveconfig=open(filename,'w+')
        print(ipaddr + " Saving running configuration to file")
        saveconfig.write(sRoutput + "\n")
        saveconfig.close()
    except:
        print(ipaddr + " is offline")
        pass

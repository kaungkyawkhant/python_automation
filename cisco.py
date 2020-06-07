#!/usr/bin/env python3
import paramiko
import sys
import time

HOST = sys.argv[1]
USER = "admin"
PASS = "P@ssw0rd"
ENABLE = "P@ssw0rd"  
PORT = 8022

def disable_paging(data):
    print("Disable paging")
    data.send("terminal length 0\n")
    time.sleep(1)
    
    # Clear the buffer on the screen
    output = data.recv(1000)
    
def exec_mode(data):
    print("Enter EXEC mode")
    data.send("enable\n")
    time.sleep(1)
    data.send("%s\n" % (ENABLE))
    time.sleep(1)
    
    # Clear the buffer on the screen
    output = data.recv(1000)
    
def send_command(data, cmd):
    print("Send: %s" % (cmd))
    data.send("%s\n" % (cmd))
    time.sleep(2)
    garbled = data.recv(65535)
    
    # output
    output = garbled.decode('UTF-8').replace("\r", "")
    print(output)

if __name__ == '__main__':
    
    # Create SSH instance
    ssh = paramiko.SSHClient()
    
    # Automatically add host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    #Inistiate SSH connection
    ssh.connect(HOST, username = USER, password = PASS, port = PORT, look_for_keys = False, allow_agent = False)
    print("Establish SSH connection to %s" % (HOST))
    
    # Establish interactive session
    data = ssh.invoke_shell()
    print("Interactive SSH session")
    
    # Clear the buffer on the screen
    data.recv(1000)
    
    # Disable paging
    disable_paging(data)
    
    # Enter EXEC mode
    exec_mode(data)

    # send command
    send_command(data, "sh ver")
    send_command(data, "sh run")
    send_command(data, "sh inv")

    # close ssh instance
    ssh.close()
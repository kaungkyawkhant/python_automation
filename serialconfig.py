import serial
from time import sleep

# Open the serial port. The settings are set to Cisco default.
serial_port = serial.Serial("COM11", baudrate=9600, timeout=None, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, xonxoff=False)
 
# Make sure there is not any lingering input - input in this case being data waiting to be received
serial_port.flushInput()
 
print(serial_port.name)
 
serial_port.write("\n".encode())

#serial_port.write("admin".encode())
#sleep(4)
#serial_port.write("\n".encode())
#sleep(4)
#serial_port.write("P@ssw0rd".encode())
#sleep(4)
#serial_port.write("\n".encode())
#sleep(4)

serial_port.write("terminal length 0\n".encode())

serial_port.write("show vtp status\n".encode())
serial_port.write("show running-config\n".encode())
sleep(1)
# serial_port.write("show ip route\n".encode())
# serial_port.write("show ip interface brief\n".encode())
# serial_port.write("show vlan brief\n".encode())
# serial_port.write("show inventory\n".encode())
# serial_port.write("show version\n".encode())
# serial_port.write("show flash\n".encode())
# serial_port.write("show etherchannel summary\n".encode())
# serial_port.write("show cdp neighbor\n".encode())
# serial_port.write("show cdp neighbor detail\n".encode())
# serial_port.write("show switch\n".encode())
# serial_port.write("show snmp user\n".encode())
# serial_port.write("show snmp group\n".encode())
# serial_port.write("show snmp engineID\n".encode())
# serial_port.write("show snmp host\n".encode())
# serial_port.write("show ntp status\n".encode())
# serial_port.write("show ntp association\n".encode())
# serial_port.write("show clock\n".encode())
# serial_port.write("show inventory\n".encode())
# serial_port.write("show vlan brief\n".encode())
# serial_port.write("write memory\n".encode())

bytes_to_read = serial_port.inWaiting()
 
# Give the line a small amount of time to receive data
sleep(20)
 
# 9600 baud is not very fast so if you call serial_port.inWaiting() without sleeping at all it will likely just say
# 0 bytes. This loop sleeps 1 second each iteration and updates bytes_to_read. If serial_port.inWaiting() returns a
# higher value than what is in bytes_to_read we know that more data is still coming in. I noticed just by doing a ?
# command it had to iterate through the loop twice before all the data arrived.
while bytes_to_read < serial_port.inWaiting():
	bytes_to_read = serial_port.inWaiting()
	sleep(3)
 
	
# This line reads the amount of data specified by bytes_to_read in. The .decode converts it from a type of "bytes" to a
# string type, which we can then properly print.
data = serial_port.read(bytes_to_read).decode()
print(data)
# This is an alternate way to read data. However it presents a problem in that it will block even after there is no more
# IO. I solved it using the loop above.
# for line in serial_port:
#print(line)




serial_port.close()

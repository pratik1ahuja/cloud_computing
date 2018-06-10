#!/usr/bin/python2

#import modules
import os
import commands
import cgi

#for the content of http server
print "Content-type:text/html"

print ""

#to scan input of user
data=cgi.FieldStorage()

#to get value of drive_name and drive_size
drive_name=data.getvalue("dn")
drive_size=data.getvalue("ds")

#to check the existing files of storage directory
st_name=commands.getoutput('ls /media/storage')

check=st_name.split('\n')

if drive_name in check:
	#if drive_name already exist
        print "soory drive already exist"

else:
	#to make a logical volume decide by user
        print commands.getoutput('sudo lvcreate --name '+drive_name+' -V'+drive_size+'GB --thin cloudst/pratik')

	#to format the drive
        print commands.getoutput('sudo mkfs.xfs /dev/cloudst/'+drive_name)

	#to make a direcory in for mounting
        print commands.getoutput('sudo mkdir /media/storage/'+drive_name)

	#mounting that drive
        print commands.getoutput('sudo mount /dev/cloudst/'+drive_name+'   /media/storage/'+drive_name)


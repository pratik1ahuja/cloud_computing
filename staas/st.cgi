#!/usr/bin/python2

import os
import commands
import cgi

print "Content-type:text/html"

print ""

data=cgi.FieldStorage()

drive_name=data.getvalue("dn")
drive_size=data.getvalue("ds")


st_name=commands.getoutput('ls /media/storage')

check=st_name.split('\n')

if drive_name in check:
        print "soory drive already exist"

else:
        print commands.getoutput('sudo lvcreate --name '+drive_name+' -V'+drive_size+'GB --thin cloudst/pratik')


        print commands.getoutput('sudo mkfs.xfs /dev/cloudst/'+drive_name)


        print commands.getoutput('sudo mkdir /media/storage/'+drive_name)

        print commands.getoutput('sudo mount /dev/cloudst/'+drive_name+'   /media/storage/'+drive_name)


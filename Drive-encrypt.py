"""
Author: Bradley T Hubbard
Project: Digital Forensics Toolkit - Drive-encrypt.py
Description: Encrypt storage drives using LUKS encryption to secure drives for the storage of forensic evidence in investigations
"""
import os
import time

def banner():
	print ("\n\n\n* Project: Digital Forensic Toolkit - Linux \n* Program: Drive-encrypt.py \n* Creater: Bradley T Hubbard \n* Signture: 3f9262ac222fb6e9cfa3b3a7a7b985b4 \n\n\n")

def luks_encrypt():
	os.system("ls /dev/")
	drive = "/dev/" + input("Which drive do you wish to encrypt: ")
	unmountdev = "sudo umount " + drive
	wipe = "sudo wipefd -a" + drive
	luksformat = "sudo cryptsetup LuksFormat" + drive
	drivename = input("Enter name for drive: ")
	luksopen = "sudo cryptsetup open" + drive + " " + drivename
	filesys = "sudo mkfs.ext4 /dev/mapper/" + drivename + " -L /mnt/" + drivename
	umountmnt = "sudo umount /mnt/" + drivename
	luksclose = "sudo cryptsetup close " + drivename

#	os.system(drive)
	print (drive)
#	os.system(unmountdev)
	print (unmountdev)
#	os.system(wipe)
	print (wipe)
#	os.system(luksformat)
	print (luksformat)
#	check drivename veriable
	print (drivename)
#	os.system(luksopen)
	print (luksopen) 
#	os.system(filesys)
	print (filesys)
#	os.system(umountmnt)
	print (umountmnt)
#	os.system(luksclose)
	print (luksclose) 

luks_encrypt()

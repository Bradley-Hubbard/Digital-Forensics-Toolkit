"""
Author: Bradley T Hubbard
Project: Forensics - Zero.py
Description: The script with automate the multiple zeroing cycles to erases a hard drive. These are been for secure deletion
before reuse or before destorying the drive. These script will use dd to zero the drive.
"""
import os
import time

def banner():
	print ("\n\n\n* Project: Digital Forensic Toolkit - Linux \n* Program: Zero.py \n* Creater: Bradley T Hubbard \n* Signture: 3f9262ac222fb6e9cfa3b3a7a7b985b4 \n\n\n")

def locate_media():
	print ("Drive Name: ")
	drivename = os.system("ls /dev/") #sd* or nvme
	print (drivename) # output content of /dev/
	zero()

def zero():
	counter = 0
	loop = 0	
	command = "sudo dd if=/dev/zero of=/dev/" + input("Enter device you wish to zero (e.g. sda of whole device or sda1 for the first partition): ") + " status=progress"
	counter = int(input("How many times do you wish to zero the drive? "))
	confirmation = "temp"	
	while confirmation != "yes":
		print (command)
		confirmation = input("Do you wish to processed(yes/no)? ")
		if confirmation == "yes":
			while loop < counter:
				print ("Round ", loop)
				#os.system(command)
				loop = loop + 1
		elif confirmation == "no":
			break
			main()
		else:
			print("Invalid Input")
			confirmation = "temp"

def main():
	menuoption = '-0'
	while menuoption != '0':
		print ("\n\n\n1 = zero\n0 = exit")
		menuoption = input("Enter selection: ")
		if menuoption == '1':
			locate_media()
		elif menuoption == '0':
			print ("Program Terminating .....\n")
			time.sleep(5)			
			print ("Goodbye\n")
		else:
			print ("Invalid Option\n")
			menuoption = '-0'

banner()
main()

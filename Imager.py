"""
Author: Bradley T Hubbard
Project: Digital Forensics Toolkit - Imager.py
Description: Hard drive imaging automation script for a live usb running linux. These was tested on kali linux. Developed for easier aquiresation of forensic images.
"""

import os
import time

def banner():
	print ("\n\n\n* Project: Digital Forensic Toolkit - Linux \n* Program: Imager.py \n* Creator: Bradley T Hubbard \n* Signture: 3f9262ac222fb6e9cfa3b3a7a7b985b4 \n\n\n")

# Identifying the target drive
def locate_media():
	print ("Drive Name:")
	drivename = os.system("ls /dev/") # sd*, nvme

	print (drivename) # output as ls

"""
The hashing function is meant for give the user a hash value to compare to the images once acquired to ensure no change to the data.
"""
def hashing():
	option = input("Do you wish to image a storage media or image file? (media/file): ")
	if option == "media":
		md5command = "sudo md5sum /dev/" + input("enter drive you wish to hash (/dev/*): ") # sudo required
	elif option == "file":
		md5command = "sudo md5sum " + input("enter file path to file (start from root '/'): ")
	
	print ("Please Standby...\n")
	print (md5command)	
	drivehash = os.system(md5command)
	print (drivehash)
	#print ("Skipping Hashing...\n")

# Imaging with DD
def imaging():
	ddcommand = "sudo dd if=/dev/" + input("enter target drive to imaging(/dev/*): ") + " of=" + input("enter path to save destination (/path/to/save/location (e.g /home/user/document/ddimage.dd)): ") + " status=progress"

	print ("Please Standby ... \n")
	print (ddcommand)
	confirmation = "temp"
	while confirmation != "yes":
		confirmation = input("Do you wish to processed(yes/no)? ")	
		if confirmation == "yes":
			os.system(ddcommand) # image targeted media
		elif confirmation == "no":
			menu()
		else:
			print ("Invalid input")
			confirmation = "temp"

def main():
	menuoption = '-0'
	while menuoption != '0':
		print ("1 = Locate Storage Media")
		print ("2 = Hash Target Media")
		print ("3 = Image Target Media")
		print ("0 = Exit\n\n\n")
		menuoption = input("Enter selection: ")
		if menuoption == '1':
			locate_media()
		elif menuoption == '2':
			hashing()
		elif menuoption == '3':
			imaging()
		elif menuoption == '0':
			print ("Program Terminating .....\n")
			time.sleep(5)			
			print ("Goodbye\n")
		else:
			print ("Invalid Option\n")
			menuoption = '-0'
banner()
main()

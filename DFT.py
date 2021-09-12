"""
Author: Bradley T Hubbard
Project: Digital Forensics Toolkit - DFT.py
Description: Combindation of all DFT script into one script.
"""

import os
import time

def banner():
	print("""
 ____  _____ ____ _____ _____ 
|  _ \|  ___/ ___|_   _|  ___|
| | | | |_ | |     | | | |_   
| |_| |  _|| |___  | | |  _|  
|____/|_|   \____| |_| |_|    
                             
	""")

	print ("\n\n\n* Project: Digital Forensic Toolkit - Linux \n* Program: DFT.py \n* Creater: Bradley T Hubbard \n* Signture: 3f9262ac222fb6e9cfa3b3a7a7b985b4 \n\n\n")

def menu():
	menuoption = '-0'
	while menuoption != '0':
		print ("\n\n\nDigital Forensics Toolkit - Menu \n1 - Image storage media \n2 - Zero storage media \n3 - Mount image file \n4 - File Search \n5 - Drive encryption - No Active \n0 - Exit \n")
		menuoption = input("Enter option: ")
		if menuoption == '1':
			imaging()
		elif menuoption == '2':
			zero()
		elif menuoption == '3':
			mount()
		elif menuoption == '4':
			file_search()
		elif menuoption == '5':
			drive_encrypt()
		elif menuoption == '0':
			exit()
		else:
			print ("Invalid Input\n")

def imaging():
	
	print ("Drive Name:")
	os.system("ls /dev/") # sd*, nvme
	
	source_device = input ("Enter path to source device (e.g. /dev/nvme0): ")
	save_location = input ("Enter path to save location and filename (e.g. /home/<user>/Desktop/<filename>): ")

	ddcommand = "sudo dd if=" + source_device + " of=" + save_location + " status=progress"
	md5command_source = "sudo md5sum " + source_device
	md5command_file = "sudo md5sum " + save_location

	print ("Please Standby... \n")
	print (ddcommand + "\n")
	print (md5command_source + "\n")
	print (md5command_file + "\n")

	confirmation = "temp"
	while confirmation != "yes":
		confirmation = input("Do you wish to processed(yes/no)? ")	
		if confirmation == "yes":
			source_hash = os.system(md5command_source) # hash source device
			print("\n")
			os.system(ddcommand) # image targeted media
			print("\n")
			image_file_hash = os.system(md5command_file) # hash dd file
		elif confirmation == "no":
			menu()
		else:
			print ("Invalid Input")
			confirmation = "temp"
	return()

def zero():

	print ("Drive Name:")
	drivename = os.system("ls /dev/") # sd*, nvme
	counter = 0
	loop = 0	
	command = "sudo dd if=/dev/zero of=/dev/" + input("\nEnter device you wish to zero (e.g. sda of whole device or sda1 for the first partition): ") + " status=progress"
	counter = int(input("\nHow many times do you wish to zero the drive? "))
	confirmation = "temp"	
	while confirmation != "yes":
		print (command)
		confirmation = input("\nDo you wish to processed(yes/no)? ")
		if confirmation == "yes":
			while loop < counter:
				print ("Round ", loop)
				#os.system(command)
				loop = loop + 1
			return()
		elif confirmation == "no":
			return()
		else:
			print("\nInvalid Input")
			confirmation = "temp"
	return()
	
def mount():

	command = "sudo losetup -P /dev/loop"+ input("Enter /dev/loop number: ") + " " + input("Input path to image from root directory: ")
	print(command)
	os.system(command)
	main()

def file_search():

	def filesearch_extension():

		file_extension = input("Enter file extension: ")

		x = input("Enter path to search: ")
		for root, dirs, files in os.walk(x):
			for file in files:
				if file.endswith(file_extension):
					print (root + '/' + file)
		return()

	def filesearch_Beginning():

		file_basename = input("Enter file basename: ")

		x = input("Enter start path to search: ")
		for root, dirs, files in os.walk(x):
			for file in files:
				if file.startswith(file_basename):
					print (root + '/' + file)
		return()

	def filesearch_Both():
		file_name = input("Enter file name with extension: ")
		x = input("Enter start path to search: ")
		for root, dirs, files in os.walk(x):
			for file in files:
				if file.startswith(file_name.split(".")[0]) and file.endswith(file_name.split(".")[1]):
					print (root + '/' + file)
		return()

	def filesearch():
		while True:
			print("\n\n\n1 = search by extension \n2 = search by basename \n3 = search by both \n0 = exit \n")
			option = input("Enter option: ")
			if option == '1':
				filesearch_extension()
			elif option == '2':
				filesearch_Beginning()
			elif option == '3':
				filesearch_Both()
			elif option == '0':
				return()
			else:
				print ("Invalid Input")

	filesearch()


banner()
menu()
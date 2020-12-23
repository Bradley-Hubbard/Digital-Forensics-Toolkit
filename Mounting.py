import os
import time

def banner():
	print ("\n\n\n* Project: Digital Forensic Toolkit - Linux \n* Program: Imager.py \n* Creater: Bradley T Hubbard \n* Signture: 3f9262ac222fb6e9cfa3b3a7a7b985b4 \n\n\n")

def mount():
	command = "sudo losetup -P /dev/loop"+ input("Enter /dev/loop number: ") + " " + input("Input path to image from root directory: ")
	print(command)
	os.system(command)
	main()
def unmount():
	option = '-0'
	while option != '0':
		option = input("1 = detach all images mount to file system \n2 = detach a chosen imaging mounted \n0 = exit\nEnter option: ")
		if option == '1':
			command = "sudo losetup -D" #This will detach all images atached
			os.system(command)
			print (command)
		elif option == '2':
			os.system("sudo losetup -a")
			command = "sudo losetup -d /dev/loop" + input("input loop number: ")
			os.system(command)
			print (command)
		elif option == '0':
			break
		else:
			print("Invalid Input")
			option = '-0'
def main():
	menuoption = '-0'
	while menuoption != '0':
		print ("\n\n\n1 = mount image\n2 = unmount image\n0 = exit")
		menuoption = input("Enter selection: ")
		if menuoption == '1':
			mount()
		elif menuoption == '2':
			unmount()
		elif menuoption == '0':
			print ("Program Terminating .....\n")
			time.sleep(5)			
			print ("Goodbye\n")
			exit()
		else:
			print ("Invalid Option\n")
			menuoption = '-0'

banner()
main()

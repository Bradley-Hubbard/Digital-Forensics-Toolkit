"""
Author: Bradley T Hubbard
Project: Digital Forensics Toolkit - File-Search.py
Description: File search is build to search file systems for a file with a file basename, extension or both.
"""

import os

def filesearch_extension():

	file_extension = input("Enter file extension: ")

	x = input("Enter path to search: ")
	for root, dirs, files in os.walk(x):
		for file in files:
			if file.endswith(file_extension):
				print (root + '/' + file)

def filesearch_Beginning():

	file_basename = input("Enter file basename: ")

	x = input("Enter start path to search: ")
	for root, dirs, files in os.walk(x):
		for file in files:
			if file.startswith(file_basename):
				print (root + '/' + file)

def filesearch_Both():
	file_name = input("Enter file name with extension: ")
	x = input("Enter start path to search: ")
	for root, dirs, files in os.walk(x):
		for file in files:
			if file.startswith(file_name.split(".")[0]) and file.endswith(file_name.split(".")[1]):
				print (root + '/' + file)

def filesearch():
	print("1 = search by extension \n2 = search by basename \n3 = search by both \n0 = exit \n")
	option = input("Enter option: ")
	if option == '1':
		filesearch_extension()
	elif option == '2':
		filesearch_Beginning()
	elif option == '3':
		filesearch_Both()
	elif option == '0':
		exit()
	else:
		filesearch()

filesearch()

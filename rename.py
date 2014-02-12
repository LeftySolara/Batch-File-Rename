# Batch file renamer

from os import chdir, getcwd, listdir, rename
from os.path import dirname, exists, expanduser, isfile, isdir
from sys import exit


def change_dir():
	""" Changes current working directory. """

	print("Enter desired directory path:")
	path = input("> ")
	chdir(path)
	print("Directory changed to {}".format(getcwd()))

def show_files():
	""" Displays files in current working directory """

	dir_list = listdir()
	print("")
	print("Files in this directory:")
	for i in dir_list:
		index = dir_list.index(i)
		if isfile(i) == True:
			print("{:>3}: {} (file)".format(index,i))
		elif isdir(i) == True:
			print("{:>3}: {} (directory)".format(index,i))
	print("")
	return dir_list

def prompt():
	""" Prompts user for options """

	print("Batch File Rename.")
	print("Current working directory: {}".format(getcwd()))
	print("Use this directory (Y/N)?")
	choice = input("> ")
	if choice.upper() == "Y":
		pass
	elif choice.upper() == "N":
		change_dir()
	else:
		print("Invalid option. Exiting...")
		exit(0)

def choose_files(files):
	""" Prompts user to choose files to edit """

	chosen = False
	while chosen == False:
		print("Enter the number of each file to edit (separated by commas) or 'a' for all.")
		choice = input("> ")
		choice_list = choice.split(",")
		chosen_files = []
		print("Files chosen:")
		if choice_list[0] == "a":
			chosen_files = [i for i in listdir()]
		else:
			for i in choice_list:
				i = int(i)
				name = files[i]
				chosen_files.append(name)
		for filename in chosen_files:
			print(filename,end=" ")
		print("")
		confirm = input("Use these files? ")
		if confirm.upper() == "Y":
			chosen = True
		elif confirm.upper() == "N":
			pass
	return chosen_files

def type_choice(file_list):
	""" Prompts for type of edit """

	edit_types = ["add","remove","replace","change case"]
	print("Perform what type of edit?")
	option = input("> ")
	if option == "add":
		add_text(file_list)
	elif option == "remove":
		try:
			remove_text(file_list)
		except ValueError:
			print("Substring not found.")
			type_choice(file_list)
	elif option == "replace":
		replace_text(file_list)

def add_text(file_list):
	""" Adds text to file names """
	print("Enter text to add to file:")
	edit = input("> ")
	for i in file_list:
		index = i.index(".")
		new_name = i[:index] + edit + i[index:]
		rename(i,new_name)

def remove_text(file_list):
	""" Removes text from file names """
	print("Enter text to remove from file:")
	edit = input("> ")
	for name in file_list:
		index = name.index(edit)
		new_name = name[:index] + name[len(edit) + index:]
		rename(name,new_name)

def replace_text(file_list):
	""" Replaces text in file names """
	print("Enter text to replace:")
	old = input("> ")
	print("Enter replacement text:")
	new = input("> ")
	for name in file_list:
		new_name = name.replace(old,new)
		rename(name,new_name)

def main():
	prompt()
	files = show_files()
	file_list = choose_files(files)
	type_choice(file_list)

if __name__ == "__main__":
	main()
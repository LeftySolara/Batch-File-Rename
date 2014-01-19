# Batch file renamer
# Future feature: select "starts with", "ends with", "contains", etc.

from os import chdir, getcwd, listdir, rename
from os.path import dirname, exists, expanduser, isfile, isdir
from sys import exit


def change_dir():
	""" Changes current working directory. """
	# Error check: invalid directory entered

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
		else:
			print("UFO")  # debugging
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

	print("Enter the number of each file to edit, separated by commas.")
	choice = input("> ")
	choice_list = choice.split(",")
	chosen_files = []
	for i in choice_list:
		i = int(i)
		name = files[i]
		chosen_files.append(name)
	return chosen_files

def type_choice(file_list):
	""" Prompts for type of edit """

	edit_types = ["add","remove","replace","change case"]
	print("Perform what type of edit?")
	option = input("> ")
	if option == "add":
		add_text(file_list)
	elif option == "remove":
		remove_text()
	elif option == "replace":
		replace_text()
	elif option == "change case":
		change_case()

def add_text(file_list):
	""" Adds text to file names """
	print("Enter text to add to file:")
	edit = input("> ")

def remove_text():
	""" Removes text from file names """

def replace_text():
	""" Replaces text in file names """

def change_case():
	""" Changes case in file names """

def main():
	prompt()
	files = show_files()
	file_list = choose_files(files)
	type_choice(file_list)

if __name__ == "__main__":
	main()
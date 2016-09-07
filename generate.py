#!python3
import random, sys # Import Stuff

# DEFAULT VARIABLES 
# YOU CAN CHANGE DEFAULTS HERE

default_length = 16 # Default Length Must be Interger
default_characters = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' # Default Chars must be String
default_error = 'Error: Something Unexpected Happened' # Default Error Must be String

# DO NOT EDIT ANY BELOW CODE

command_list = sys.argv # Take Arguments from Command Line
# Syntax for Command Line Use:
# > python generate.py [NUMBER OF RESUTS] [LENGTH OF RESULTS (OPTIONAL)]
# Example:
# > python generate.py 10 12
# This would produce 10 random strings, each with 12 random characters. 
#
# If no arguments are supplied then 'python generate.py' will simply launch
# the guided generator

try:
	command_list[1] # Test if Command Line Recieved Arguments
	command_line = True # If first Argument Recieved set command_line as True
except (ValueError, IndexError) as Error: # if the command line did not recieve arguments
	command_line = False # Set command_line as False

def generator(size=default_length, chars=default_characters): # Generate from this String
	return ''.join(random.choice(chars) for _ in range(size)) # for character in string pick randomly


if command_line == False: # if not run from command line ask user questions
	chars = input('How many Characters? (Blank for {}) '.format(str(default_length))) # Ask user for # of Chars
	max_num = input('How many codes to Generate? (Blank for Infinite) ') # Ask user for # of codes
else: # If it is run from command line.
	try:
		chars = command_list[2] # try to get the # of characters
	except (ValueError, IndexError) as Error: # if not set
		chars = default_length # set chars to 16

	max_num = command_list[1] # set max_num from the console arguments (Checked on line 6)

num = 1 # Set num = 1

if chars == '': # Check if Chars is blank
	chars = '{}'.format(default_length) # if blank default to 16
if max_num == '': # Check if Max_Num is blank
	max_num = False # If blank default to False for Unlimited

try:
	while num <= int(max_num) or max_num == False: # Check if num less than max_num or if unlimited
		print(generator(size=int(chars))) # Print the output from generator() function
		num += 1 # add one to num var
except: # If any errors occure print this
	print('\n{}'.format(default_error))
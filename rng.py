"""rng.py - random number generator"""

# imports
import sys
import collections
from msvcrt import getch
#import pickle
import pprint
import random


# constants


# module level objects



### functions
def d4():
	return random.randint(1, 4)

def d6():
	return random.randint(1, 6)

def d8():
	return random.randint(1, 8)

def d10():
	return random.randint(1, 10)

def d12():
	return random.randint(1, 12)

def d20():
	return random.randint(1, 20)

def d100():
	return random.randint(1, 100)


def recursive_print_rolls(number_to_print, die_func, die_string):
	x = number_to_print - 10
	if x < 0:
		rolls_to_print = diceFunc(x, die_func)
		
		# the number of spaces in the beginning depend on the die
		sys.stdout.write(' ')

		sys.stdout.write(str(x))
		sys.stdout.write(die_string)
		sys.stdout.write(': ')
		print rolls_to_print, "sum = ", sum(rolls_to_print)


def print_usage():
	print '\nUsage: python', sys.argv[0]


# superset of menu items
#L      - List data items in current area
#+      - List next page of data items
#-      - List previous page of data items
#1 to # - Display data item
# REMOVED -> #E      - Edit the last displayed data item
#S      - Search...
#Up arw - Select a new area...
#M      - Show this menu
#ESC to exit
def print_menu():
	print "\nMenu:"
	
	# menu and exit are always available
	print '''       M      - Show this menu
       R      - Roll dice
       ESC    - Exit program'''
	return 0  # success


def print_prompt(suppress_menu_tip=False):
	# the trailing comma supresses the newline that normally occurs
	if suppress_menu_tip:
		print "\n[", sys.argv[0], "] Choose action > ",
	else:
		print "\n[", sys.argv[0], "] Choose action, or 'm' for menu of choices > ",



### main
if __name__ == '__main__':
	# check command line
	if len(sys.argv) > 1:
		print_usage()
		sys.exit()
	else:
		print sys.argv[0], ': starting...'
	
	# do other init actions
	random.seed()
	# define helper function
	def diceFunc(num, func):
		tempList = []
		for _ignored in xrange(num):
			tempList.append(func())
		return tuple(tempList)

	
	print_menu()
	menu_shown = True
	
	while True:
		print_prompt(menu_shown)
		menu_shown = False
		
		key = ord(getch())
		if key == 0:
			#print '\nDEBUG: got 0x0'
			key = ord(getch())
			# now you can look for the code for special keys like 'f1', 'f2', etc. if you have need
		elif key == 224:
			#print '\nDEBUG: got 0x224'
			key = ord(getch())
			# now you can look for the code for special keys like 'up arrow', 'insert', 'delete', etc. if you have need
			if key == 72: # hex 0x48  # up arrow key
				# nothing here yet
				pass
		elif key == 3:  # Control - C
			sys.exit()
		elif key == 48:  # hex 0x30 is number 0
			# ignore the number zero
			pass
		elif key == 49:  # hex 0x31 is number 1
			# echo the 1
			sys.stdout.write('1')
			# get second digit
			second_digit = getch()
			second_digit_code = ord(second_digit)
			if second_digit_code >= 48 and second_digit_code <= 57:
				number_of_rolls = int('1' + second_digit)
				print "{} - Roll {} dice\n".format(second_digit, number_of_rolls)
				recursive_print_rolls(number_of_rolls, d4, 'd4')
				#printXd4 = diceFunc(number_of_rolls, d4)
				#sys.stdout.write(' ')
				#sys.stdout.write(str(number_of_rolls))
				#sys.stdout.write('d4: ')
				#print printXd4, "sum = ", sum(printXd4)
			else:
				print '\nAfter pressing "1" press another number to complete a 2 digit number'
		elif key == 50:  # hex 0x32 is number 2
			print '2 - Roll two dice'
			print2d4 = (d4(), d4())
			print ' 2d4:', print2d4, " sum =", sum(print2d4)
			print2d6 = (d6(), d6())
			print '     2d6:', print2d6, " sum =", sum(print2d6)
			print2d8 = (d8(), d8())
			print '         2d8:', print2d8, " sum =", sum(print2d8)
			print2d10 = (d10(), d10())
			print '             2d10:', print2d10, " sum =", sum(print2d10)
			print2d12 = (d12(), d12())
			print '                 2d12:', print2d12, " sum =", sum(print2d12)
			print2d20 = (d20(), d20())
			print '                     2d20:', print2d20, " sum =", sum(print2d20)
			print2d100 = (d100(), d100())
			print '                         2d100:', print2d100, " sum =", sum(print2d100)
		elif key == 51:  # hex 0x33 is number 3
			print '3 - Roll three dice'
			def threeDice(func):
				return (func(), func(), func())
			print3d4 = threeDice(d4)
			print ' 3d4:', print3d4, " sum =", sum(print3d4)
			print3d6 = threeDice(d6)
			print '     3d6:', print3d6, " sum =", sum(print3d6)
			print3d8 = threeDice(d8)
			print '         3d8:', print3d8, " sum =", sum(print3d8)
			print3d10 = threeDice(d10)
			print '             3d10:', print3d10, " sum =", sum(print3d10)
			print3d12 = threeDice(d12)
			print '                 3d12:', print3d12, " sum =", sum(print3d12)
			print3d20 = threeDice(d20)
			print '                     3d20:', print3d20, " sum =", sum(print3d20)
			print3d100 = threeDice(d100)
			print '                         3d100:', print3d100, " sum =", sum(print3d100)
		elif key == 52:  # hex 0x34 is number 4
			print '4 - Roll four dice'
			print4d4 = diceFunc(4, d4)
			print ' 4d4:', print4d4, " sum =", sum(print4d4)
			print4d6 = diceFunc(4, d6)
			print '     4d6:', print4d6, " sum =", sum(print4d6)
			print4d8 = diceFunc(4, d8)
			print '         4d8:', print4d8, " sum =", sum(print4d8)
			print4d10 = diceFunc(4, d10)
			print '             4d10:', print4d10, " sum =", sum(print4d10)
			print4d12 = diceFunc(4, d12)
			print '                 4d12:', print4d12, " sum =", sum(print4d12)
			print4d20 = diceFunc(4, d20)
			print '                     4d20:', print4d20, " sum =", sum(print4d20)
			print4d100 = diceFunc(4, d100)
			print '                         4d100:', print4d100, " sum =", sum(print4d100)
		elif key == 53:  # hex 0x35 is number 5
			print '5 - Roll five dice'
			print5d4 = diceFunc(5, d4)
			print ' 5d4:', print5d4, " sum =", sum(print5d4)
			print5d6 = diceFunc(5, d6)
			print '     5d6:', print5d6, " sum =", sum(print5d6)
			print5d8 = diceFunc(5, d8)
			print '         5d8:', print5d8, " sum =", sum(print5d8)
			print5d10 = diceFunc(5, d10)
			print '             5d10:', print5d10, " sum =", sum(print5d10)
			print5d12 = diceFunc(5, d12)
			print '                 5d12:', print5d12, " sum =", sum(print5d12)
			print5d20 = diceFunc(5, d20)
			print '                     5d20:', print5d20, " sum =", sum(print5d20)
			print5d100 = diceFunc(5, d100)
			print '                         5d100:', print5d100, " sum =", sum(print5d100)
		elif key == 54:  # hex 0x36 is number 6
			print '6 - Roll six dice'
			print6d4 = diceFunc(6, d4)
			print ' 6d4:', print6d4, " sum =", sum(print6d4)
			print6d6 = diceFunc(6, d6)
			print '     6d6:', print6d6, " sum =", sum(print6d6)
			print6d8 = diceFunc(6, d8)
			print '         6d8:', print6d8, " sum =", sum(print6d8)
			print6d10 = diceFunc(6, d10)
			print '             6d10:', print6d10, " sum =", sum(print6d10)
			print6d12 = diceFunc(6, d12)
			print '                 6d12:', print6d12, " sum =", sum(print6d12)
			print6d20 = diceFunc(6, d20)
			print '                     6d20:', print6d20, " sum =", sum(print6d20)
			print6d100 = diceFunc(6, d100)
			print '                         6d100:', print6d100, " sum =", sum(print6d100)
		elif key == 55:  # hex 0x37 is number 7
			print '7 - Roll seven dice'
			print7d4 = diceFunc(7, d4)
			print ' 7d4:', print7d4, " sum =", sum(print7d4)
			print7d6 = diceFunc(7, d6)
			print '     7d6:', print7d6, " sum =", sum(print7d6)
			print7d8 = diceFunc(7, d8)
			print '         7d8:', print7d8, " sum =", sum(print7d8)
			print7d10 = diceFunc(7, d10)
			print '             7d10:', print7d10, " sum =", sum(print7d10)
			print7d12 = diceFunc(7, d12)
			print '                 7d12:', print7d12, " sum =", sum(print7d12)
			print7d20 = diceFunc(7, d20)
			print '                     7d20:', print7d20, " sum =", sum(print7d20)
			print7d100 = diceFunc(7, d100)
			print '                         7d100:', print7d100, " sum =", sum(print7d100)
		elif key == 56:  # hex 0x38 is number 8
			print '8 - Roll eight dice'
			print8d4 = diceFunc(8, d4)
			print ' 8d4:', print8d4, " sum =", sum(print8d4)
			print8d6 = diceFunc(8, d6)
			print '     8d6:', print8d6, " sum =", sum(print8d6)
			print8d8 = diceFunc(8, d8)
			print '         8d8:', print8d8, " sum =", sum(print8d8)
			print8d10 = diceFunc(8, d10)
			print '             8d10:', print8d10, " sum =", sum(print8d10)
			print8d12 = diceFunc(8, d12)
			print '                 8d12:', print8d12, " sum =", sum(print8d12)
			print8d20 = diceFunc(8, d20)
			print '                     8d20:', print8d20, " sum =", sum(print8d20)
			print8d100 = diceFunc(8, d100)
			print '                         8d100:', print8d100, " sum =", sum(print8d100)
		elif key == 57:  # hex 0x39 is number 9
			print '9 - Roll nine dice'
			print9d4 = diceFunc(9, d4)
			print ' 9d4:', print9d4, " sum =", sum(print9d4)
			print9d6 = diceFunc(9, d6)
			print '     9d6:', print9d6, " sum =", sum(print9d6)
			print9d8 = diceFunc(9, d8)
			print '         9d8:', print9d8, " sum =", sum(print9d8)
			print9d10 = diceFunc(9, d10)
			print '             9d10:', print9d10, " sum =", sum(print9d10)
			print9d12 = diceFunc(9, d12)
			print '                 9d12:', print9d12, " sum =", sum(print9d12)
			print9d20 = diceFunc(9, d20)
			print '                     9d20:', print9d20, " sum =", sum(print9d20)
			print9d100 = diceFunc(9, d100)
			print '                         9d100:', print9d100, " sum =", sum(print9d100)
		elif key == 43 or key == 61: # hex 0x2b or 0x3d  # +/= key
			# nothing here yet
			pass
		elif key == 95 or key == 45: # hex 0x5f or 0x2d  # _/- key
			# nothing here yet
			pass
		elif key == 108: # hex 0x6c  # l key (lower case L)
			# nothing here yet
			pass
		elif key == 109: # hex 0x6d  # m key
			print_menu()
			menu_shown = True
		elif key == 114: # hex 0x72  # r key
			print 'r - Roll dice'
			print ' d4:', d4()
			print '        d6:', d6()
			print '               d8:', d8()
			print '                      d10:', d10()
			print '                              1st d20:', d20()
			print '                              Adv/Disadv d20:', d20()
			print '                                      d%:', d100()
			print '[0.0, 1.0):', random.random()
		elif key == 27: # hex 0x1b  # ESC key
			break
		#print '\nDEBUG key =', key
	
	print '\nDone.'

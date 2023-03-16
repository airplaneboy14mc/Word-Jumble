#print blank line
print()

#import random
import random
import os
import time


#define main function
def main():
	try:
		#tell user about the game
		print("Welcome to Word Jumble!")
		print(
		 "This will select a random word from a predefined list of words and jumble them up.\nYou will then have to guess the word based off of the jumbled letters."
		)
		#create tuple
		words = init_tuple()
		#choose the word
		rand_cat = random.choice(words)
		rand_word = random.choice(rand_cat)
		#check the category
		category = check_cat(rand_cat)
		#print out the category
		print(f"\nThe category is {category}.")
		#check if correct later
		correct = rand_word
		jumble = ""
		while rand_word:
			position = random.randrange(len(rand_word))
			jumble += rand_word[position]
			rand_word = rand_word[:position] + rand_word[(position + 1):]
		print(f"The jumble is {jumble}.")
		#call guess function
		guess(correct, rand_word)
		#check if user would like to run again
		run_again()
	except KeyboardInterrupt:
		clear()
		print(error_color.warn + 'KeyboardInterrupt is disabled.' + error_color.endc)
		time.sleep(1)
		clear()
		print()
		main()


#define init_tuple function
def init_tuple():
	deserts = ('Chocolate', 'Oreos', 'Cannoli', 'Carrot Cake', 'Swedish Fish',
	           'Pecan Pie', 'Cheesecake', 'Creme Brulee', 'Black Forest Gateau',
	           'Gelato', 'Ice Cream', 'Pumpkin Pie', 'Cherry Pie')
	meats = ('Chicken', 'Beef', 'Turkey', 'Pork', 'Ham', 'Venison', 'Buffalo',
	         'Salmon', 'Goose', 'Boar', 'Tuna', 'Crab', 'Bison', 'Calamari',
	         'Octopus')
	fruits = ('Banana', 'Dragon Fruit', 'Orange', 'Kiwi', 'Apple', 'Mango',
	          'Pineapple', 'Nectarine', 'Raspberry', 'Strawberry', 'Cherry',
	          'Grapefruit', 'Star Fruit', 'Pear', 'Lemon', 'Blueberry', 'Date',
	          'Honeydew', 'Tomato', 'Passion Fruit')
	vegetables = ('Cucumber', 'Bell Pepper', 'Carrot', 'Romain Lettuce',
	              'Spinach', 'Kale', 'Celery')
	categories = (deserts, meats, fruits, vegetables)
	return categories


#define check_cat function
def check_cat(category):
	#determine the category to be returned
	if "Oreos" in category:
		return "Deserts"
	elif "Chicken" in category:
		return "Meats"
	elif "Banana" in category:
		return "Fruits"
	elif "Cucumber" in category:
		return "Vegetables"
	else:
		return "Could not determine category."


#define guess function
def guess(correct, word):
	#get the user's guess
	user_input = ""
	while correct != user_input:
		user_input = input("Enter your guess here: ")
		if correct != user_input:
			#if incorrect, run again
			print("\nYou did not guess correctly. Please try again.\n")
		else:
			print("\nYou guessed correctly!\n")


#function to clear the screen
def clear():
	os.system('clear')


#function to control running again
def run_again():
	#ask if they would like to run again
	again = input("\n\nWould you like to run the program again? (Y/N) ")
	#clear the screen and reprint out
	if again == "Y" or again == "y":
		clear()
		print()
		main()
	else:
		#let user know program is exiting and clear screen, then KeyboardInterrupt
		print(error_color.red + "\nExiting.\n" + error_color.endc)
		time.sleep(0.5)
		clear()
		KeyboardInterrupt


class error_color:
	red = '\u001b[31m'
	warn = '\033[93m'
	endc = '\033[0m'


#call main
main()

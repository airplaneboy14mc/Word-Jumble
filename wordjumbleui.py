import tkinter as tk
import os
import time
import random
from tkinter import messagebox

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
def main():
    words = init_tuple()
    rand_cat = random.choice(words)
    rand_word = random.choice(rand_cat)
    category = check_cat(rand_cat)
    correct = rand_word
    jumble = ""
    while rand_word:
        position = random.randrange(len(rand_word))
        jumble += rand_word[position]
        rand_word = rand_word[:position] + rand_word[(position + 1):]

    def guess(correct, word):
        guess = str(entry.get())
        if correct != guess:
            messagebox.showerror('Incorrect', 'The word is not correct')
        else:
            messagebox.showinfo('Correct', 'The word is correct!')
        quit()
        main()
        
    def quit():
        main_window.destroy()

    main_window = tk.Tk()
    main_window.title('Word Jumble Game')
    main_window.geometry('420x275')
    main_window.resizable(False, False)
        
    top_frame = tk.Frame(main_window)
    bottom_frame = tk.Frame(main_window)
        
    top_frame.pack(side='top')
    bottom_frame.pack(side='bottom')
        
    top_label = tk.Label(top_frame, text='Word Jumble Game', font=('Comic Sans MS', 38))
    top_label.pack(side='top')
    enter_guess = tk.Label(bottom_frame, text='Enter your guess:', font=('Comic Sans MS', 16))
    enter_guess.pack(side='top', padx=10)
    entry = tk.Entry(bottom_frame)
    entry.pack(side='top')
    cat_label = tk.Label(top_frame, text=f'Category: {category}', font=('Comic Sans MS', 22))
    cat_label.pack(side='top')
    jumble_label = tk.Label(top_frame, text=f'Jumble: {jumble}', font=('Comic Sans MS', 22))
    jumble_label.pack(side='top')

    enter_button = tk.Button(bottom_frame, text='Enter', command=lambda: guess(correct, rand_word))
    enter_button.pack(side='left', pady=5, padx=3)
    quit_button = tk.Button(bottom_frame, text='Quit', command=quit)
    quit_button.pack(side='left', pady=5, padx=3)
    about_button = tk.Button(bottom_frame, text='About', command=lambda: messagebox.showinfo('About','This game chooses a word from a category, then jumbles the letters and lets the user guess the word'))
    about_button.pack(side='left', pady=5, padx=3)

    main_window.mainloop()

main()
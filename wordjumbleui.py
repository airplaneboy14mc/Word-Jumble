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
    try:
        def quit():
            main_window.destroy()
        
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
            if jumble == correct:
                quit()
                main()
            else:
                pass

        def guess():
            guess = str(entry.get())
            if correct != guess:
                messagebox.showerror('Incorrect', 'The word is not correct.')
            else:
                messagebox.showinfo('Correct', 'The word is correct!')
                quit()
                main()
        
        def handler(e):
            guess = str(entry.get())
            if correct != guess:
                messagebox.showerror('Incorrect', 'The word is not correct.')
            else:
                messagebox.showinfo('Correct', 'The word is correct!')
                quit()
                main()
        
        def exit_program(e):
            quit()
        
        def settings():
            def destroy_settings(e):
                settings.destroy()
            settings = tk.Tk()
            settings.title('Settings')
            settings.geometry('420x275')
            settings.resizable(False, False)
            settings.bind('<Escape>', destroy_settings)
            settings.bind('<Delete>', destroy_settings)
            top_frame = tk.Frame(settings)
            top_frame.pack(side='top', pady=4)
            left_side_frame = tk.Frame(settings)
            left_side_frame.pack(side='left', padx=4)
            right_side_frame = tk.Frame(settings)
            right_side_frame.pack(side='right', padx=4)
            settings_label = tk.Label(top_frame, text='Settings', font=('Comic Sans MS', 32))
            settings_label.pack(side='top')
            controls_button = tk.Button(left_side_frame, text='Controls', font=('Comic Sans MS', 16), command=controls)
            controls_button.pack(side='top')
            controls_label = tk.Label(right_side_frame, text='Edit the keyboard controls \nused in the app.', font=('Comic Sans MS', 14))
            controls_label.pack(side='top')
            font_button = tk.Button(left_side_frame, width=7, text='Fonts', font=('Comic Sans MS', 16), command=lambda: print('e'))
            font_button.pack(side='top')
            font_label = tk.Label(right_side_frame, text='Edit the fonts used in the program.', font=('Comic Sans MS', 14))
            font_label.pack(side='top')

            settings.mainloop()
            
        def controls():
            def destroy_cont(e):
                cont.destroy()
            cont = tk.Tk()
            cont.title('Controls')
            cont.geometry('420x275')
            cont.resizable(False, False)
            cont.bind('<Escape>', destroy_cont)
            cont.bind('<Delete>', destroy_cont)
            top_frame = tk.Frame(cont)
            left_frame = tk.Frame(cont)
            right_frame = tk.Frame(cont)
            top_frame.pack(side='top')
            left_frame.pack(side='left')
            right_frame.pack(side='right')
            controls_label = tk.Label(top_frame, text='Controls', font=('Comic Sans MS', 32))
            controls_label.pack(side='top')
            
            cont.mainloop()

        main_window = tk.Tk()
        main_window.title('Word Jumble Game')
        main_window.geometry('420x275')
        main_window.resizable(False, False)
        main_window.bind('<Return>', handler)
        main_window.bind('<Escape>', exit_program)
        main_window.bind('<Delete>', exit_program)
        photo = tk.PhotoImage(file='wordjumbleicon.png')
        main_window.wm_iconphoto(True, photo)
            
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

        controls_button = tk.Button(bottom_frame, text='Settings', font=('Comic Sans MS', 16), command=settings)
        controls_button.pack(side='left', pady=5, padx=3)
        about_button = tk.Button(bottom_frame, text='About', font=('Comic Sans MS', 16), command=lambda: messagebox.showinfo('About','This game chooses a word from a category, then jumbles the letters and lets the user guess the word'))
        about_button.pack(side='left', pady=5, padx=3)
        

        main_window.mainloop()
    except NameError:
        quit()

main()
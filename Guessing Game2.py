import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random

def guess_the_number():
    # Generate a random number within the specified range
    random_number = random.randint(min_number, max_number)
    
    # Initialize variables
    attempts = 0
    
    # Function to handle user guesses
    def check_guess():
        nonlocal attempts
        try:
            # Get user input
            user_guess = int(guess_entry.get())
            attempts += 1
            
            # Check if the guess is correct
            if user_guess == random_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number correctly in {attempts} attempts!")
    
                
            elif user_guess < random_number:
                messagebox.showinfo("Too Low", "Too low! Try again.")
            else:
                messagebox.showinfo("Too High", "Too high! Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
    
  
    # Create the main application window
    root = tk.Tk()
    root.title("Guessing Game")
    
    # to set background color
    root.minsize(450,450)
    root.config(bg= "#FFAF45")
    
    
    # Create a label widget
    instructions_label = tk.Label(root, text=f"Guess the number between {min_number} and {max_number}!")
    instructions_label.pack(pady=20)
    
    # Create an entry widget for user input
    guess_entry = tk.Entry(root)
    guess_entry.pack(pady=5)
    
    # Create a button widget to submit the guess
    guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
    guess_button.pack(pady=5)
    
    # Start the Tkinter event loop
    root.mainloop()

# Main function to start the game
if __name__ == "__main__":
    min_number = 1  # Minimum number in the range
    max_number = 10  # Maximum number in the range
    guess_the_number()

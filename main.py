import tkinter as tk
import random

def play():
    user_choice = user_entry.get().lower().strip()
    if user_choice not in ['rock', 'paper', 'scissors']:
        result_label.config(text="Invalid input! Choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You won!'
    else:
        return 'You lost!'

window = tk.Tk()
window.title('Rock-Paper-Scissors')

user_label = tk.Label(window, text='Choose rock, paper, or scissors:', font='bold')
user_label.pack(pady=5)
user_entry = tk.Entry(window)
user_entry.pack(pady=5)
play_button = tk.Button(window, text='Play', command=play)
play_button.pack(pady=5)

result_label = tk.Label(window, font='bold')
result_label.pack(pady=10)

window.mainloop()

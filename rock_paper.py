import random
from tkinter import *

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#c634eb")

# Global variables to keep track of scores
user_score = 0
computer_score = 0

# Dictionary for choice values
choices = {
    "rock": 1,
    "paper": 2,  
    "scissors": 3
}

# Function to get computer's choice
def get_computer_choice():
    choice_num = random.randint(1,3)
    if choice_num == 1:
        computer_choice = "rock"
    elif choice_num == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    return computer_choice

# Function to determine and display game result
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = "It's a tie!"

    if user_choice == "rock":
        if computer_choice == "paper":
            result = "You lose! Paper covers rock"
            computer_score += 1
        elif computer_choice == "scissors":
            result = "You win! Rock smashes scissors" 
            user_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            result = "You win! Paper covers rock"
            user_score += 1
        elif computer_choice == "scissors":
            result = "You lose! Scissors cut paper"
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            result = "You lose! Rock smashes scissors"
            computer_score += 1
        elif computer_choice == "paper":
            result = "You win! Scissors cut paper"
            user_score += 1

    result_text.config(text="You chose "+user_choice+(". Computer chose "+computer_choice+". "+result))
    score_text.config(text="Your score: "+ str(user_score)+". Computer score: "+str(computer_score)+"." )


# Function to exit the game 
def exit_app():
    root.destroy()

# Function to reset the game scores  
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_text.config(text="Your score: 0. Computer score: 0.")

# User choice buttons
rock_button = Button(root, text="Rock", padx=20, pady=10, bg="#F08080", command=lambda:play_game("rock"))    
paper_button = Button(root, text="Paper ", padx=20, pady=10, bg="#ADD8E6", command=lambda:play_game("paper"))
scissors_button = Button(root, text="Scissors", padx=20, pady=10, bg="#90EE90", command=lambda:play_game("scissors"))

# Result text 
result_text = Label(root, text="", font=("Consolas", 12), bg="#ADD8E6", justify=LEFT)

# Score text
score_text = Label(root, text="Your score: 0. Computer score: 0.", font=("Consolas", 12), bg="#ADD8E6", justify=LEFT)   

# Reset game button
reset_button = Button(root, text="Reset Scores", padx=10, pady=5, bg="#FFE4E1", command=reset_game)

# Exit button
exit_button = Button(root, text="Exit Game", padx=10, pady=5, bg="#D3D3D3", command=exit_app)

# Layout widgets in grid
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10) 
scissors_button.grid(row=0, column=2, padx=10, pady=10)

result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
score_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

reset_button.grid(row=3, column=0, padx=10, pady=10)
exit_button.grid(row=3, column=2, padx=10, pady=10)

root.mainloop()
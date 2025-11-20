# ************************************Mini Project : Rock Paper Scissors****************************

# Key Python Topics:
# OOP (Classes, Methods)
# Modules (Importing)
# Random Number Generation (random.choice())
# User Input and Validation
# Conditional Logic
# Loops (while)
# Data Structures (Dictionaries)
# Game Logic


# What You Will Create:
# A Rock Paper Scissors game where the user plays against the computer, with a menu, game logic, and score tracking.

# Instructions:
# Create a directory for the game.
# Create rock-paper-scissors.py (for menu, input, and summary).
# Create game.py (for game logic).


# Part I - game.py
# Step 1: Create the Game Class

import random

class Game:
    def __init__(self):
        pass

# Step 2: Implement get_user_item Method
# Create a method called get_user_item(self).
# Ask the user to select an item (rock/paper/scissors).

    def get_user_item(self):
        user_answer = input('Please, select one item rock/paper/scissors: ')
        return user_answer

# Step 3: Implement get_computer_item Method
# Create a method called get_computer_item(self).
# Randomly select an item (rock/paper/scissors).
# Return the computer’s item.

    def get_computer_item(self):
        item_list = ['rock', 'paper', 'scissors']
        computer_answer = random.choice(item_list)
        return computer_answer

# Step 4: Implement get_game_result Method
# Create a method called get_game_result(self, user_item, computer_item).
# Take user_item and computer_item as parameters.
# Determine the result of the game based on the rules of Rock Paper Scissors.
# Return “win”, “draw”, or “loss”.

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'scissors' and computer_item == 'paper') or \
            (user_item == 'rock' and computer_item == 'scissors') or \
            (user_item == 'paper' and computer_item == 'rock'):
            return 'win'
        else:
            return 'loss'

# Step 5: Implement play Method
# Create a method called play(self).
# Call get_user_item() to get the user’s choice.
# Call get_computer_item() to get the computer’s choice.
# Call get_game_result() to determine the result.
# Print the outcome of the game (user’s choice, computer’s choice, result).
# Return the result (“win”, “draw”, or “loss”) as a string.

    def play(self):
        user_item = self.get_user_item()
        computer_item= self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print (f'user’s choice: {user_item}, computer’s choice: {computer_item}, result: {result}')
        return result

if __name__ == "__main__":
    game = Game()
    game.play()
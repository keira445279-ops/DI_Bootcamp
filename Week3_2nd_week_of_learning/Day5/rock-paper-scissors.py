
from game import Game

# Step 6: Implement get_user_menu_choice Function
# Create a function called get_user_menu_choice().
# Display the menu options (“Play a new game”, “Show scores”, “Quit”).
# Get the user’s choice.
# Validate the input (e.g., check if it’s one of the valid options).
# Return the user’s choice.

def get_user_menu_choice():
    print('What option would you like to choose:')
    print('1. Play a new game')
    print('2. Show scores')
    print('3. Quit')

    while True:
        user_choice = input('Print the number of option, that you would like to choose (from 1 to 3): ')
        if user_choice in ('1', '2', '3'):
            return int(user_choice)
        print('Invalid option. Try again')
        
# Step 7: Implement print_results Function
# Create a function called print_results(results).
# Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
# Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
# Thank the user for playing.

def print_result(results):
    print(f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
    print("Thank you for the game. See you soon!")

# Step 8: Implement main Function
# Create a function called main().
# Pepeatedly show the menu until the user chooses to exit.
# Call get_user_menu_choice() to get the user’s choice.
# If the user chooses to play a game:
# Create a Game object.
# Call the play() method of the Game object.
# Store the result of the game in a dictionary (e.g., results).
# If the user chooses to exit:
# Call print_results() to display the game summary.
# Exit the program.

def main():

    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        # print("\nDEBUG — showing menu")
        choice = get_user_menu_choice()
        if choice == 1:
            game = Game()
            result = game.play()
            # print("DEBUG — result returned by play():", result)
            results[result] += 1
        elif choice == 2:
            print_result(results) 
        elif choice == 3:
            print_result(results)
            break

if __name__ == "__main__":
    main()                


    
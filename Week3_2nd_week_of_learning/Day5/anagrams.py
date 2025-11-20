import MP_Anagram_checker
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'sowpods.txt')

def show_menu():
    print('What would you like to do?')
    print('1. Input a word')
    print('2. Exit')

while True:

    show_menu()

    user_option_choice = int(input('Print the number of option, that you would like to choose (from 1 to 2): '))
    if user_option_choice == 1:
        user_word = input ('Please, enter a word: ').strip()
        if not user_word.isalpha() or len(user_word.split()) != 1:
            print('Input must be a single word with alphabetic characters only.')
            continue
        print(f'Your input word is: {user_word}')
        checker = MP_Anagram_checker.AnagramChecker(file_path)
        anagrams = checker.get_anagrams(user_word)
        if anagrams:
            print(f"""YOUR WORD: {user_word.upper()}
                      this is a valid English word.
                      Anagrams for your word: {anagrams}""")
        else:
            print(f'No anagrams found for "{user_word}".')
    else: 
        break

import random
import os
import sys
import time

words = ["ESOPHADOS", "LINEAR", "NONLINEAR", "STATIC", "DYNAMIC",
        "DATA", "TYPE", "ARRAY", "LINKED", "LIST",
        "STACKS", "QUEUES", "TREES", "GRAPHS", "HASHING",
        "STRUCTURE", "ALGORITHM", "ANALYSIS", "GREEDY",
        "RECURSIVE", "BACKTRACKING", "SORTING", "RANDOMIZED",
        "SEARCH", "BINARY", "INTERVAL", "BUBBLE", "INSERTION",
        "SELECTION", "MERGE", "QUICK", "HEAP", "BUCKET",
        "RADIX", "HEAP", "MEMOIZATION", "TABULATION", "NESTED"
        ]

def scramble_word(word):
    # Convert the word to a list of characters
    char_list = list(word)

    # Fisher-Yates Shuffle Algorithm
    for i in range(len(char_list) - 1, 0, -1):
        j = random.randint(0, i) # Generate random index.
        char_list[i], char_list[j] = char_list[j], char_list[i] # Swap the value of index i and index j

    # Convert the list back to a string
    scrambled_word = ''.join(char_list)
    if scrambled_word == word:
        scramble_word(word)
    else:
        return scrambled_word

def get_correct_word_position(word, guess):
    feedback = ''

    # Ensure that the lengths match
    guess = guess.ljust(len(word), '_')

    # Iteration algorithm
    for i in range(len(word)):
        if word[i] == guess[i]:
            feedback += guess[i]
        else:
            feedback += "_"

    return feedback

def generate_hint(feedback, word, numberOfUsedHint):
    new_hint = ''

    # Iteration algorithm
    for i in range(len(word)):
        if feedback[i] == "_" and numberOfUsedHint > 0:
            new_hint += word[i]
            numberOfUsedHint -= 1
        else:
            new_hint += "_"
    
    return new_hint

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')






while True:
    try:
        # Welcome Screen
        print("---------------------------------------------")
        print("      Welcome to Word Jungle Game!")
        print("To start, press 1 and 0 to exit the program.")
        print("---------------------------------------------")
        print("Enter choice: ", end="")
        choice = int(input())

        if choice == 0:
            clear_screen()
            print("\nExiting the program. Goodbye!")
            sys.exit()
        # Game Loop
        while choice == 1:
            clear_screen()
            print("----------------------------------------------------------")
            print("             Welcome to the WORD JUNGLE GAME!\n")
            print("  In this game, you have to guess the following")
            print("  scrambled word to advance your level. Each completion")
            print("  of the level, you will be rewarded with a 1 point hint")
            print("  that you can use to guess the scrambled word.")
            print("----------------------------------------------------------")
            time.sleep(8)
            level = 1
            total_hint = 5
            alreadyUsed = set()
            while True:
                clear_screen()
                wordToBeGuess = random.choice(words)
                while wordToBeGuess in alreadyUsed: # Loop as long as the value of wordToBeGuess is already in the alreadyUsed variable(set).
                    wordToBeGuess = random.choice(words)    # Random pick of word.
                alreadyUsed.add(wordToBeGuess)  # Insert the value of wordToBeGuess in the alreadyUsed variable(set) in order to keep track all the words that already used.
                scrambled_word = scramble_word(wordToBeGuess)
                feedback = '_' * len(wordToBeGuess)  # Initialize feedback with underscores
                numberOfUsedHint = 0

                while True:
                    print("---------------------------------------")
                    print("----------- Word Jungle Game ----------")
                    print("---------------------------------------")
                    print(f"                LEVEL {level}")
                    print(f"             Hints left: {total_hint}\n")
                    print(f"        Guess the word: {scrambled_word}")
                    print("---------------------------------------")
                    print("Enter (2) for Hint.\nEnter (0) to exit.")
                    print("---------------------------------------")
                    userGuess = input("Enter your answer: ").upper()
                    print("---------------------------------------")

                    clear_screen()  # Clear the screen after user input

                    # Check if the user wants a hint
                    if userGuess == '2':
                        if total_hint > 0:
                            total_hint -= 1
                            numberOfUsedHint += 1
                            hint = generate_hint(feedback, wordToBeGuess, numberOfUsedHint)
                            print("---------------------------------------")
                            print(f"Hint: {hint}")
                        else:
                            print("---------------------------------------")
                            print("No more hints left.")
                            print("---------------------------------------")
                            time.sleep(3)
                            clear_screen ()  # Wait for 2 seconds
                        continue

                    # Check if the user's word guess matches the word to be guessed
                    if userGuess == wordToBeGuess:
                        print("---------------------------------------")
                        print(f"Excellent! {wordToBeGuess} is correct.")
                        print("---------------------------------------")
                        total_hint += 1 # add 1 hint every correct answer.
                        if level != 10:
                            level += 1
                        else:   # Reset all the value of level, total_hint and alreadyUsed.
                            print("You have reached the maximum level.")
                            print("Levels will now be reset")
                            print("---------------------------------------")
                            level = 1
                            total_hint = 5
                            alreadyUsed = set()
                        break  # Break from the inner loop to generate a new word
                    elif userGuess == '0':
                        print("Thank you for playing WORD JUNGLE GAME!")
                        sys.exit()
                    elif not userGuess.isalpha() or len(userGuess) != len(wordToBeGuess):
                        print("Invalid input.")
                        time.sleep(3)
                        clear_screen()

                    elif not userGuess:
                        print("Nice try! Try to guess again.")

                    elif not set(userGuess).issubset(wordToBeGuess):
                        print("Your guess contains letters not in the scrambled word.")
                        time.sleep(3)
                        clear_screen()

                    elif any(userGuess.count(char) > wordToBeGuess.count(char) for char in userGuess):
                        print("Your guess contains repeated letters not present in the scrambled word.")
                        time.sleep(3)
                        clear_screen()

                    else:
                        feedback = get_correct_word_position(wordToBeGuess, userGuess)
                        print("---------------------------------------")
                        print(f"Keep trying! {feedback} are in correct placement.")
                        time.sleep(3)

                play_again = input("Do you want to play another round? (Y/N): ").upper()
                while play_again != 'N' and play_again != 'Y':
                    clear_screen()
                    print("WARNING: Invalid choice!\n---------------------------------------")
                    print(f"Excellent! {wordToBeGuess} is correct.")
                    print("---------------------------------------")
                    play_again = input("Do you want to play another round? (Y/N): ").upper()
                if play_again == 'N':
                    clear_screen()
                    print("Thank you for playing WORD JUNGLE GAME!!")
                    sys.exit()  # Exit the outer loop if the user does not want to play another round
    except(ValueError): # Perform this condition if the value of choice(user input) is not an integer.
        clear_screen()
        print("WARNING: Invalid choice!")
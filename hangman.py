#Step 1 
import random

#word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.



from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6

from hangman_art import logo, stages
print(logo)
#step 2
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


display = []
for letter in chosen_word:
    display += "_"



#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

end_of_game = False

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    if guess in display:
        print(f"You've already gussed {guess}")
    #check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter   

    print(display)

    if guess not in chosen_word:
        print(f"you guessed {guess}, thats not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
        
    
#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])

#step 3
#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.        

#step 4
#TODO-8: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-9: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.

#TODO-10: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining. 

#Step 5
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
 #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.   
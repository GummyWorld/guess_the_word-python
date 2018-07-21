import random
import string

#variables
word = "text"
word_line = "text"
word_list = {"list"}

tries_left = 3
tries = 3
coins = 50
len_list = 0
xWord = 2

print("Welcome to the game!")

#writing and reading files
#This prints every line in the .txt file
with open ("stringstorage.txt","r") as f:
    for line in f:
        print(line)
        
word_select = input("Choose a category by typing the row number: ")

with open ("stringstorage.txt","r") as f:
    #Setting variables
    word_line = f.readlines()[int(word_select)].rstrip()  #Get rid of "/n"
    word_list = word_line.split(" ")  #Splits the string by a space 
    print (word_list)

randIndice = random.randint(2, len(word_list))
word = word_list[randIndice]

print ("This word contains " + str(len(word)) + " letters")

#Word guessing begins
clue_letter = word[0] + word[-1]

#As the player is in the range of the number of tries
for tries in range(tries):
    guess_word = input("What word am I thinking?")

    #Adds coins, break loop
    if guess_word in word:
        tries_left += 1
        print ("You are correct!")
        coins += 10
        break
    
    #When the player guesses the word wrong    
    else:
        tries += 1
        print ("Try Again")
    
    if tries == 2 :
        clue = input("Would you like a hint for 40 coins? Type \'n\' or \'y\'")
    
        if clue == 'y':
            print ("The first and last letter of the word is " + clue_letter)
            coins -= 10
            
        else:
            print ("Let's continue!")

   
    if tries == 3 and guess_word != word:
        print("Unlucky!")
        print("The word was", word)

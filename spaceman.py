import random
import string

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    # f = open('words2.txt', 'r') # words2.txt file
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for char in secret_word:
      if char != "\n":
        if char not in letters_guessed:
          return False
    # if it makes it all the way without hitting False, then the word was guessed
    print("You win!!")
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores. For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    display_word = "_" * (len(secret_word))
    for i in range(len(secret_word)):
      if secret_word[i] in letters_guessed:
        display_word = display_word[0:i] + secret_word[i] + display_word[i:-1]
    return display_word

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word: return True
    else: return False
    

def draw_spaceman(guesses_remaining, word_length):
    spaceman = [
        "     O",
        "     O\n     |",
        "     O\n     |\n    /",
        "     O\n     |\n    /|",
        "     O\n     |\n    /|\ ",
        "     O\n     |\n    /|\  \n    /",
        "     O\n     |\n    /|\  \n    / \ ",
    ]
    # spaceman = [" O", 
    #             " |",
    #             "/|\ ",
    #             "/ \ "]
    # spaceman.append(char)
    # for i in range(word_length - guesses_remaining):
    #     print(spaceman[i])
    idx = word_length - guesses_remaining - 1
    if idx < len(spaceman):
        print(spaceman[idx])


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    
    letters_left = string.ascii_lowercase
    def get_letters_not_guessed(letters_left):
        for letter in letters_guessed:
            if letter in letters_left:
                idx = letters_left.index(letter)
                # letters_left = letters_left[:idx] + letters_left[idx + 1:] #same effect as using replace()
                letters_left = letters_left.replace(letter, "")
        return letters_left
    
    guesses_remaining = len(secret_word)
    word_guessed = False

    #TODO: show the player information about the game according to the project spec
    print("-----------------------------------------------")
    print("Welcome to Spaceman! Guess the letters in the secret word to win!")
    print(f"The secret word contains: {len(secret_word)} letters")
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("-----------------------------------------------")
    while word_guessed == False:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = input("Enter a letter: ")

        if (guesses_remaining < 1):
            print("you lose!")
            print(f"The secret word was: {secret_word}")
            ask_play_again(word_guessed)
            break

        # if guess == secret_word: print("you winnnn!!")
        if  guess == "":
            print("Must enter a letter.")
            continue
        elif len(guess) > 1 or type(guess) != str: 
            print("Must be a single letter.")
            print(f"You have {guesses_remaining} guesses left")
            guesses_remaining -= 1
            draw_spaceman(guesses_remaining, len(secret_word))
            continue
        elif guess in letters_guessed: 
            print("Already guessed that letter. Guess another letter.")
            continue

        else: letters_guessed.append(guess)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word): 
            print("Got one!")
        else:
            print("Guessed wrong..")
            guesses_remaining -= 1
            draw_spaceman(guesses_remaining, len(secret_word))

        print(f"You have {guesses_remaining} guesses left")
        #TODO: show the guessed word so far
        print(f"Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}")
        print(f"These letters haven't been guessed yet: {get_letters_not_guessed(letters_left)}")

        #TODO: check if the game has been won or lost
        word_guessed = is_word_guessed(secret_word, letters_guessed)
        if word_guessed == True:
            ask_play_again(word_guessed)


def ask_play_again(word_guessed):
    response = input("play again? y/n: ")
    if response == "y":
        start_game()
    else: return

def start_game():
    secret_word = load_word()
    spaceman(secret_word)

start_game()


#These function calls that will start the game
# print(secret_word)

# answer = get_guessed_word(secret_word, ['c', 'o', 'm', 't', 'g', 'y', 'a', 'q', 'd', 'e', 'h', 'j', 'i'])
# print(secret_word, answer)

# print(is_guess_in_word("a", secret_word))


""" 
Spaceman Pseudocode:

DEFINE a function to load a word randomly from a .txt file for the user to guess




 """
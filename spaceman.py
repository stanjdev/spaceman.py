import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    # words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
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
    display_word = "_" * (len(secret_word) - 1)
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


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    attempts = 0
    word_guessed = False

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman! Guess the letters in the secret word to win!")
    print(f"The secret word contains: {len(secret_word)} letters")
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("----------------------------------")
    while word_guessed == False:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = input("Enter a letter: ")
        attempts += 1
        print(f"attempts: {attempts}")
        if (attempts >= len(secret_word)):
            print("you lose!")
            break

        # if guess == secret_word: print("you winnnn!!")
        elif len(guess) > 1 or type(guess) != str or guess == "": 
            print("Must be a single letter.")
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

        #TODO: show the guessed word so far
        print(f"Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}")

        #TODO: check if the game has been won or lost
        word_guessed = is_word_guessed(secret_word, letters_guessed)


#These function calls that will start the game
secret_word = load_word()
# print(secret_word)

# answer = get_guessed_word(secret_word, ['c', 'o', 'm', 't', 'g', 'y', 'a', 'q', 'd', 'e', 'h', 'j', 'i'])
# print(secret_word, answer)

# print(is_guess_in_word("a", secret_word))

spaceman(secret_word)
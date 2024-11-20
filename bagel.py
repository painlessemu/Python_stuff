import random

NUM_DIGITS = 3 
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.By James Matyka
          
I am thinking of a {}-digit number with no repeated digits
Try and guess what it is you fucking dumb ass. Here are some clues:
when i say:     That Means:
    Pico        One digit is correct but in the wrong postition.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
          
For example, if the secret number was 246 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS) )
    
    while True: #the main game loop
        secretNum = getsecretNum()
        print('I have thought up a number')
        print(' You have {} number if guesses to get it '.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS: #or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # User is correct, break out of this loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {},'.format(secretNum))

        #Ask if they want to play again
        print('You want to play again you idiot? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    
def getsecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789abcdefg') #create list of digits 0 - 9
    random.shuffle(numbers) #Shuffle them into random order.

    #Get the first NUM_DIGITS in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair"""
    if guess == secretNum:
        return 'You Got it! Maybe your parents are somewhat proud.'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # No correct digits at all
    else:
        # Sort the clues into alphabetical order so their orignal order
        # Doesnt give information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
    




if __name__== '__main__':
    main()

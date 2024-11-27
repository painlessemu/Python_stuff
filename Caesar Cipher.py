"""Caesar Cipher, by James 
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip
except ImportError:
    pass  # if pyperclip is not installed, do nothing, It's no biggie

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Cesar Cipher, by Painless')
print('The Caeser cipher encrypts letters by shifting them over by a')
print('key number, For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted to D, and so on.')

# let the user enter if they are encrypting or decrypting:
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response .startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter the key to use:
while True: #Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey})')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0<= int(response) < len(SYMBOLS):
        key = int(response)
        break

# LEt the user enter the message to encrypt/decrypt
print(f'Enter the message to {mode}')
message = input('> ')

# Caesat cipher only works on uppercase letters:
message = message.upper()

## Stores the encrypted.decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol) # Get the number of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # Handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        
        # Add encrypted/decrupted number's symbol to translated:
        translated += SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated += symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard')
except:
    pass # Do nothing if pyperclip wasn't installed.
        

    
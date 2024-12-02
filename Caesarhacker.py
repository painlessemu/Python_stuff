"""Caesar Cipher Hacker, by James Matyka
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by James Matyka')

# Let the user specify the message to hack:
print('Enter the encrypted Ceasar cipher message to hack.')
message = input('> ')

#Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the umber of the symbol
            num -= key # Decrypt the number

        # Handle the wrap-around if num is less than 0:
        if num < 0:
            num += len(SYMBOLS)

        # Add decrypted number's symbol to translated:
        translated += SYMBOLS[num]
    else:
        # Just add the symbol wihout decrypting
        translated += symbol

    # Display the key being tsted, along with its decrypted text:
    print(f'Key #{key}:{translated}')
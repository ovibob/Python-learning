try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal

symbols= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Let the user enter if they are encrypting or decrypting:
while True: # Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break

# Let the user enter the key to use:
while True: # Keep asking until the user enters a valid key.
    max_key = len(symbols) - 1
    print('Please enter the key (0 to {}) to use:'.format(max_key))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}:'.format(mode))
message = input('> ')
message = message.upper() # Caesar cipher only works on uppercase letters:

# Stores the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in symbols:
        # Get the encrypted (or decrypted) number for this symbol
        num = symbols.find(symbol) # Get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if num is larger than the length of symbols or less than 0:
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + symbols[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.


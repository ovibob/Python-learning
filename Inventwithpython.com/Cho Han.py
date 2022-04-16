import random
import sys

JAPANESE_NUMBERS = {1:'ICI', 2:'NI', 3:'SAN', 4:'SHI', 5:'GO', 6:'ROKU'}

print()
print('''In Cho-Han, a traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.''')
print()

purse = 5000
print('You have', purse, 'euro. How much do you bet? (or QUIT) ')
while True: # main game loop for placing the bet
    pot = input('> ')
    if pot.upper() == "QUIT":
        print('Thanks for playing!')
        sys.exit()
    elif not pot.isdecimal():
        print("Please enter a number: ")
    elif int(pot) > purse:
        print('You do not have enough money to place that bet!')
    else: # this is a valid bet
        pot = int(pot) # convert po to an integer
        break  # exit the loop once a valid bet is placed

# roll the dice
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print('The dealer swirls the cup and you hear the rattle of dice.')
print('The dealer slams the cup on the floor, still covering the')
print('dice and asks for your bet.')
print()
print('    CHO (even) or HAN (odd)?')

# let the player bet cho or han
while True:
    bet = input('> ').upper()
    if bet != "CHO" and bet != "HAN":
        print('Please enter either "CHO" or "HAN"!')
        continue
    else:
        break

# reveal the dice results:
print('The dealer lifts the cup to reveal:')
print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
print('    ', dice1, '-', dice2)

# determine if the player won
rolls_even = (dice1 + dice2) % 2 == 0
if rolls_even:
    correct_bet = "CHO"
else:
    correct_bet = 'HAN'

# display the bet result
player_won = bet == correct_bet
if player_won:
    print('You won! You take', pot, 'euro.')
    purse = purse + pot  # Add the pot from player's purse.
    print('The house collects a', pot // 10, 'euro fee.')
    purse = purse - (pot // 10)  # The house fee is 10%.
else:
    purse = purse - pot  # Subtract the pot from player's purse.
    print('You lost!')

# check if the player has run out of money
if purse == 0:
    print('You have run out of money!')
    print('Thanks for playing!')
    sys.exit()

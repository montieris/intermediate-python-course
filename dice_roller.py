import random

def main():
    #ievada loopu daudzumu
    dice_rolls = int(input('How many dice would you like to roll? '))
    #variablis cik katrā rollaa var liels skaitlis izkrist
    dice_size = int(input('How many sides are the dice? '))

    #nodefinee nulles veertiibu
    dice_sum = 0

    #loopu cikls
    for i in range(0,dice_rolls):

        #mainiigais roll = random(plugin).randint(plugin.funkcija) (1 - dice_size)
        roll = random.randint(1,dice_size)

        #summa = iepriekšējā loopa summa + jaunais roll
        dice_sum = dice_sum + roll

        # if / elseif  / else check-print
        if roll == 1:
            print(f'You rolled a {roll} an unlucky roll ..')
        elif roll == dice_size:
            print(f'You rolled a {roll} a lucky strike!')
        else:
            print(f'You rolled a {roll}')

    # kopsumma no visiem loopiem
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
    main()

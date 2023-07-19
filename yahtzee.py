import random

def main():
    while True:
        action = input('("?" for help) Input: ')

        if action == "?":
            print('\nType "n" when prompted for input to roll a new set of 5 dices\nor\ntype the the numbers rolled to reroll them. For example, if you rolled 1,2,3,3,6 type "3,6" to roll a single 3 and the 6.\nNote: please type the numbers ffrom smallest to largest in the syntax shown (with commas)\n')

        if action == 'n':
            dice, reroll = [random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1], 2
            dice.sort()
            print(f'\nYou rolled a set of dice. Rerolls remaining: {reroll}\n==================================\n{dice}\n==================================\n')

        else:
            action.replace(' ','').split(',')
            for i in range(len(action)):
                for j in range(5):
                    if action[i] == dice[j]:
                        dice[j] = random.choice(range(6))+1
                        action[i]






def calculations():
    pass


if __name__ == '__main__':
    main()
import random

def main():
    while True:
        action = input('("?" for help) Input: ')

        if action == "?":
            print('\nType "n" when prompted for input to roll a new set of 5 dices\nor\ntype the the numbers rolled to reroll them. For example, if you rolled 1,2,3,3,6 type "3,6" to roll a single 3 and the 6.\nNote: Please type of the numbers using the syntax shown (with ocmmas). And randomness is random - which means you might end up having the same number. That is not a bug!\n')

        elif action == 'n':
            dice, reroll = [random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1], 2
            dice.sort()
            print(f'\nYou rolled a set of dice. Rerolls remaining: {reroll}\n==================================\n{dice}\n==================================\n')

        else:
            if reroll == 0:
                print('You have already used both of your rerolls. Please create a new set of dice by typing "n" when propted for input.')
                continue
            action = action.replace(' ','').split(',')
            for i in range(len(action)):
                for j in range(5):
                    if int(action[i]) == dice[j]:
                        dice[j] = random.choice(range(6))+1
                        break
            reroll -= 1
            dice.sort()
            print(f'\nYou rolled a set of dice. Rerolls remaining: {reroll}\n==================================\n{dice}\n==================================\n')






def calculations():
    pass


if __name__ == '__main__':
    main()
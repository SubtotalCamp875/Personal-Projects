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
            print(calculations(dice))


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
            print(calculations(dice))



def calculations(dice):
    solutions, chain = 'With the above dices, you can score with:\n', 0
    if '1' in dice: solutions += 'Aces\n'
    if '2' in dice: solutions += 'Twos\n'
    if '3' in dice: solutions += 'Threes\n'
    if '4' in dice: solutions += 'Fours\n'
    if '5' in dice: solutions += 'Fives\n'
    if '6' in dice: solutions += 'Sixes\n'
    for i in range(len(dice)):
        if i == 0: pass
        if dice[i] == dice[i-1]: chain += 1
        else: chain = 0


if __name__ == '__main__':
    main()
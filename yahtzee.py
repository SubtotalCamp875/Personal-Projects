import random, time
from colorama import Fore

def main():
    while True:
        action = input('("?" for help) Input: ')
        print(' ')

        if action == "?":
            print('\n-Type "n" when prompted for input to roll a new set of 5 dices\n-Type "e" to exit the code\n-Type "s" to set a dice roll of your choice\nAnd/Or\ntype the the numbers rolled to reroll them. For example, if you rolled 1,2,3,3,6 type "3,6" to roll a single 3 and the 6.\nNote: Please type of the numbers using the syntax shown (with ocmmas). Randomness is random - which means you might end up having the same number. That is not a bug!\n')


        elif action == 'n':
            dice, reroll = [random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1], 2
            dice.sort()
            print(Fore.RED + f'You rolled a set of dice. Rerolls remaining: {reroll}')
            time.sleep(1)
            print(Fore.YELLOW + f'==================================\n{dice}\n==================================')
            time.sleep(1)
            print(Fore.GREEN + calculations(dice) + Fore.WHITE)

        elif action == 'e': break
        elif action == 's':
            dice, reroll = input('input 5 numbers to act as your hand: ').replace(' ','').split(','), 2
            print(Fore.MAGENTA + 'The dices are now set as:\n' + Fore.YELLOW + f'==================================\n{dice}\n==================================' + Fore.WHITE)

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
            if reroll == 0: print(Fore.MAGENTA + 'This is your FINAL HAND')
            time.sleep(1)
            print(Fore.RED + f'You rolled a set of dice. Rerolls remaining: {reroll}')
            time.sleep(1)
            print(Fore.YELLOW + f'==================================\n{dice}\n==================================')
            time.sleep(1)
            print(Fore.GREEN + calculations(dice) + Fore.WHITE)


def calculations(dice):
    chain, chain_list, total, solutions, words_list, s_straights_list, l_straights_list = 1, [], 0, 'With the above dices, you can score with:\n', ['Aces','Twos','Threes','Fours','Fives','Sixes'], [[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 5, 6]], [[1 ,2 ,3 ,4 ,5 ],[2, 3, 4, 5, 6]]


    for i in range(7): #tests for numbers 1-6 and the total of that number
        if i == 0: continue
        for j in range(5):
            if i == int(dice[j]):
                total += i
        if total != 0:
            solutions += f'{words_list[i-1]} for: {total}\n'
            total = 0


    for i in range(5): #stores the amount fo numbers that are in a row within a list then reset
        if i == 0: continue
        if dice[i] == dice[i-1]:
            chain += 1
            if i != 4: continue
        if dice[i] != dice[i-1] and chain >= 2:
            chain_list.append(chain)
            chain = 1
            continue
        chain_list.append(chain)
    if chain == 1:
        chain_list.append(chain)


    if 3 in chain_list: solutions += f'Three of a kind for: {sum(dice)}\n'
    if 4 in chain_list: solutions += f'Four of a kind for: {sum(dice)}\n'
    if chain_list == [3, 2] or chain_list == [2, 3]: solutions += 'Full house for: 25\n'
    for i in range(3):
        if str(s_straights_list[i]).replace('[','').replace(']','') in str(dice):
            solutions += 'Small straight for: 30\n'
            break
    for i in range(2):
        if str(l_straights_list[i]).replace('[','').replace(']','') in str(dice): solutions += 'Large straight for: 40\n'
    if 5 in chain_list: solutions += 'Yahtzee for: 50\n'

    return(solutions)



def sum(dice):
    sum = 0
    for i in range(len(dice)):
        sum += int(dice[i])
    return(sum)



if __name__ == '__main__':
    main()
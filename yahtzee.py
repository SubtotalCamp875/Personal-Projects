import random

def main():
    action = input('("?" for help) Input: ')

    if action == "?":
        print('Type "n" when prompted for input to roll and new set of 5 dices or type the the numbers rolled to reroll them. For example, if you rolled 1,2,3,3,6 type "3,6" to roll a single 3 and the 6')

    if action == 'n':
        print(f'======================\n{random.choice(range(6))+1})


def calculations():




if __name__ == "__main()__":
    main()
import random

def main():
    total = 0
    for i in range(25):
        value, power = random.choice(range(1,10)), random.choice(range(2,4))
        answer = input(f'{value}^{power} = ')
        if answer == "e": break
        if answer.isnumeric() == False or int(answer) != value**power: print(f'{value}^{power} = {value**power}')
        else:
            total += 1
            continue
    print(f'{total}/25')

if __name__ == '__main__':
    main()
import random

def main():
    total = 0
    for i in range(25):
        value, power = random.choice(range(1,10)), random.choice(range(2,4))
        answer = input(f'{value}^{power} = ')
        if answer == "e": break
        if innumberic(answer) == False: print(f'{value}^{power} = {value**power}')
        if int(answer) == value**power:
            total += 1
            continue
        else: print(f'{value}^{power} = {value**power}')
    print(f'{Total}/25')

if __name__ == '__main__':
    main()
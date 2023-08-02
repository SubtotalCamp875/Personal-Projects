import random

def main():
    diff = input('Difficukty: ')
    total = 0

    match diff:
        case 'E'|'e'|'easy':
            for i in range(25):
                value, power = random.choice(range(1,10)), random.choice(range(2,4))
                answer = input(f'{value}^{power} = ')
                if answer == "e": break
                if answer.isnumeric() == False or int(answer) != value**power: print(f'{value}^{power} = {value**power}')
                else:
                    total += 1
                    continue

        case 'm'|'M'|'medium':
            for i in range(25):
                power = random.choice(range(2,4))
                if power == 2: value = random.choice(range(11,21))
                if power == 3: value = random.choice(range(2,10))

                answer = input(f'{value}^{power} = ')
                if answer == "e": break
                if answer.isnumeric() == False or int(answer) != value**power: print(f'{value}^{power} = {value**power}')
                else:
                    total += 1
                    continue

        case 'H'|'h'|'hard':
            for i in range(25):
                power = random.choice(range(2,4))
                if power == 2: value = random.choice(range(11,21))
                if power == 3: value = random.choice(range(11,21))

                answer = input(f'{value}^{power} = ')
                if answer == "e": break
                if answer.isnumeric() == False or int(answer) != value**power: print(f'{value}^{power} = {value**power}')
                else:
                    total += 1
                    continue


    print(f'{total}/25')

if __name__ == '__main__':
    main()
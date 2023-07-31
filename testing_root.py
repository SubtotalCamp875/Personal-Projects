import random

def main():
    while True:
        value = random.choice(range(1,10))
        answer = input(f'{value}^2 = ')
        if answer == "e": break
        if int(answer) == value**2: continue
        else: print(f'{value}^2 = {value**2}')

if __name__ == '__main__':
    main()
def main():
    for i in range(2):
        for j in range(20): print(f'{j} = {j**(i+2)}')
        sep()

def sep(): print('============')

if __name__ == '__main__':
    main()
def main():
    for i in range(3):
        for j in range(10):
            print(f'{j} = {j**(i+1)}')
        sep()

def sep(): print('============')

if __name__ == '__main__':
    main()
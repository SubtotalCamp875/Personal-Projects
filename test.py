
def main():
    mode = input('1.) build drum\n2.) shift numbers\n~')
    if mode == '1':
        output = r'y_{beat}=-\frac{1}{6.02}'
        equation = 'g\left(x,\frac{6.02}{6.02+6.02+6.02},1\right)'
        values = input('input: ')
        values = values.split(', ')


        def isEven(num):
            if num % 2 == 0:
                return True
            else: return False

        for i in range(len(values)):
            if isEven(i): sign = '+'
            else: sign = '-'
            output += sign+r'g\left(x,\frac{6.02}{6.02+6.02+6.02},'+str(values[i])+r'\right)'
            print(i)

        print(output)


    if mode == '2':
        values = input('input: ')
        values = values.split(', ')
        shift = input('shift amount: ')
        for i in range(len(values)):
            print(f'{float(values[i])+shift}, ', end='')


main()

"""
1, 1.75, 2, 2.5, 3, 3.5, 4, 4.25, 5, 5.75, 6, 6.5, 7, 7.5, 8, 8.25, 8.5, 8.75, 9.0, 9.75, 10.0, 10.5, 11.0, 11.5, 12.0, 12.25, 13.0, 13.75, 14.0, 14.5, 15.0, 15.5, 16.0, 16.25, 16.5, 16.75, 17, 17.27, 17.5, 17.75, 19
"""
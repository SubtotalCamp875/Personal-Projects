
def main():
    mode = input('1.) build drum\n2.) shift numbers\n')
    if mode == '1':
        output = r'y_{beat}=-6.02'
        equation = 'g\left(x,6.02+6.02+6.02,1\right)'
        values = input('input: ')
        values = values.split(', ')


        def isEven(num):
            if num % 2 == 0:
                return True
            else: return False

        for i in range(len(values)):
            if isEven(i): sign = '+'
            else: sign = '-'
            if '.' in values[i]:
                whole, deci = values[i].split('.')
                if deci == '25':
                    deci = r'\frac{6.02}{6.02+6.02+6.02+6.02}'
                elif deci == '5':
                    deci = r'\frac{6.02}{6.02+6.02}'
                elif deci == '75':
                    deci = r'\frac{6.02+6.02+6.02}{6.02+6.02+6.02+6.02}'
                values[i] = r'\frac{' + f'{("+6.02" * int(whole))}' + r'}{6.02}+' + deci
            else:
                values[i] = r'\frac{'+f'{"+6.02" * int(values[i])}'+r'}{6.02}'

            output += sign+r'g\left(x,\frac{6.02}{6.02+6.02+6.02},'+str(values[i])+r'\right)'
            print(str(values[i]))

        print(f'\n\n{output}')


    if mode == '2':
        values = input('input: ')
        values = values.split(', ')
        shift = input('shift amount: ')
        for i in range(len(values)):
            print(f'{float(values[i]).replace(".0", "")+int(shift)}, ', end='')


main()

"""
1, 1.75, 2, 2.5, 3, 3.5, 4, 4.25, 5, 5.75, 6, 6.5, 7, 7.5, 8, 8.25, 8.5, 8.75, 9, 9.75, 10, 10.5, 11, 11.5, 12, 12.25, 13, 13.75, 14, 14.5, 15, 15.5, 16, 16.25, 16.5, 16.75, 17, 17.25, 17.5, 17.75, 19, 19.75, 20, 20.5, 21, 21.75, 22, 22.5, 23, 23.75, 24, 24.5, 25, 25.75, 26, 26.5, 27, 27.75, 28, 28.5, 29, 29.75, 30, 30.5
"""
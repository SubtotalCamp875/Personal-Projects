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

"""
1, 1.75, 2, 2.5, 3, 3.5, 4, 4.25, 5, 5.75, 6, 6.5, 7, 7.5, 8, 8.25, 8.5, 8.75, 9
"""
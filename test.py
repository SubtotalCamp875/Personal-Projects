
"""
import string

all = dict(zip(string.ascii_letters,range(53)))

def decode(value, all):
    answer = ''

    for i in range(len(value)):
        if value[i].isnumeric() == True: answer += ' '
        else: answer += f'{all[value[i]]}'
    print(f'{value} = {answer}')


print(all)
decode('jSHRt6QbkZY', all)
decode('North', all)
decode('South', all)
decode('East', all)
decode('West', all)
decode('SHRZY', all)
decode('TEU',all)
decode('teu',all)
"""

x = []
print(len(x))
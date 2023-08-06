import string

value, answer = 'jSHRt6QbkZY', ''
all = dict(zip(string.ascii_letters,range(52)))
for i in range(len(value)):
    if value[i].isnumeric() == True:
        answer += f'{value[i]}, '
    else:
        answer += f'{all(value[i])}, '
print(answer)
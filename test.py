"""
x = "1:2,3:4,5:6"
x = x.split(',')
print(x)
for i in range(len(x)):
    x[i] = x[i].split(':')
print(x)
print(x[1][0], x[1][1])
print(len(x))
"""
for i in range(2):
    print(i)
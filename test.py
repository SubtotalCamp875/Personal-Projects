x = "1:2,3:4,5:6"
x = x.split(',')
print(x)
for i in range(len(x)):
    x[i] = x[i].split(':')
print(x)
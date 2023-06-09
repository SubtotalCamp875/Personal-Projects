values = ["1","1.5","2","2.5","3","3.5","4"]
x = dict(zip("abcdefg",values))
a = "abcd"
a_dummy = []

for i in range(len(a)):
    if a[i] in ["a","b","c","d","e","f","g"]:
        a_dummy.append(x[a[i]])

print(a_dummy)
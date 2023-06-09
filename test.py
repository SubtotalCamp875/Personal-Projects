x = dict(zip("abcdefg","1234567"))
a = "abcd"
a_dummy = []

for i in range(len(a)):
    if a[i] in ["a","b","c","d","e","f","g"]:
        a_dummy[i] = list.append(x[a[i]])

print(a_dummy)
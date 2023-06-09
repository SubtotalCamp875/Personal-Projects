x = dict(zip("abcdefg","))
a = "abcd"
a_dummy = []

for i in range(len(a)):
    if a[i] in ["a","b","c","d","e","f","g"]:
        a_dummy.append(x[a[i]])

print(a_dummy)
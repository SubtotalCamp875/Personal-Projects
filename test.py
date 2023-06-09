x = dict(zip("abcdefg","1234567"))
a = "abcd"
for i in range(len(a)):
    if a[i] == ["a","b","c","d","e","f","g"]:
        a[i] = list(x[a[i]])

print(a)
values = ["1","1.5","2","2.5","3","3.5","4"]
x = dict(zip("abcdefg",values))
a = "abcd"
a_dummy = []

for i in range(len(a)):
    if a[i] in ["a","b","c","d","e","f","g"]:
        a_dummy.append(x[a[i]])

def request_input():
    sign, a, b, steps = list(input("sign (1=+, 0=-): ")), str(input("input of change in height: ")).replace(" ","").split(","), str(input("input of distance: ")).replace(" ","").split(",")
    return(sign, a, b, steps)

print(request_input())

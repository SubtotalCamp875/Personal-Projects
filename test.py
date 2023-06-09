def main():
    sign_dummy, a, steps = [], [], ["1","1.5","2","2.5","3","3.5","4"]
    notes = dict(zip("abcdefg",steps))
    a_dummy = input("a: ")
    for i in range(len(a_dummy)):
        print(a_dummy[i])
        print(notes["b"])
        if a_dummy[i] in ["a","b","c","d","e","f","g"]: a.append(notes[a[i]])
        else: return(print("please input notes"))

main()
def main():
    english = input("Enter a sentence in English: ")
    englist, platin = english.split(" "), ""
    for i in range(len(englist)):
        prefix = ""
        if englist[i][0].lower().strip not in ["a", "e", "i", "o", "u"]:
            prefix = englist[i][0]
            print("true")
        englist_index = str(englist[i]).replace(prefix, "", 1) + prefix + "ay"
        platin = platin + englist[i] + " "
    print(platin)


def ListToString():
    pass


main()
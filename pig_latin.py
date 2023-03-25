def main():

    english = input("Enter a sentence in English: ")
    englist, platin, punctuation = english.split(" "), "", [".", ",", "!", "?", ";", ":", '"', "'", "(", ")", "[", "]"]
    for i in range(len(englist)):

        prefix = ""
        if englist[i][0].lower().strip not in ["a", "e", "i", "o", "u"]:
            prefix = englist[i][0]

        for j in englist[i]:
            if j in punctuation:
                englist
        englist_index = str(englist[i]).replace(prefix, "", 1) + prefix + "ay"


        platin = platin + englist_index + " "
    print(platin)


def ListToString():
    pass


main()
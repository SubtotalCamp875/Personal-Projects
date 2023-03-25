def main():
    english = input("Enter a sentence in English: ")
    englist, platin, punctuation = english.split(" "), "", [".", ",", "!", "?", ";", ":", '"', "'", ")", "]"]

    for i in range(len(englist)):
        prefix, suffix = "", ""
        if englist[i][0].lower() not in ["a", "e", "i", "o", "u"]:
            prefix = englist[i][0]
            if englist[i][0].lower() in ['"', "(", "'", "["]:
                prefix = englist[i][1]

        for j in englist[i]:
            if j in punctuation:
                suffix += j
                englist[i] = englist[i].replace(j, "")

        platin += " " + str(englist[i]).replace(prefix, "", 1) + prefix.lower() + "ay" + suffix

    return(platin)

while True:
    print(main(), end="\n")
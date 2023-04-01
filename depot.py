import math

def main():
    selection = input(f"Please select a department: \n1. Paint\n2. Flooring\n3. Lighting\n").strip().lower()

    match selection:
        case "1" | "paint":
            try:
                length, walls = input('Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), float(input("How many walls will you be painting? "))
                area = walls * float(length[0]) * float(length[1])
                cans = math.ceil(area/350)
            except IndexError: print("You provided invalid syntax.")
            print(f"You will need {cans} cans of paint for {area*walls} square inches of wall. \nEach can of paint will cost $25. \nYour total cost will be {cans*25}.\nYou will have {cans*size-area} inches of paint left over")

        case "2" | "flooring":
            pass
        case "3" | "lighting":
            pass


    return(area)




main()
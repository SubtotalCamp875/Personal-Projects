import math

def main():
    selection = input(f"Please select a department: \n1. Paint\n2. Flooring\n3. Lighting\n").strip().lower()

    match selection:
        case "1" | "paint":
            try:
                area = input('Please input values in forms of "1x2" inches: ').replace(" ", "").split("x")
                area = float(input("How many walls will you be painting? ")) * float(area[0]) * float(area[1])
                cans = math.ceil(area/x)
            except IndexError: print("You provided invalid syntax.")
            print(f"You will need {cans} cans of paint for {area} inches of wall. \nEach can of paint will cost $25. \nYour total cost will be {cans*25}.\n")
        case "2" | "flooring":
            pass
        case "3" | "lighting":
            pass


    return(area)




main()
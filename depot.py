def main():
    selection = input(f"Please select a department: \n1. Paint\n2. Flooring\n3. Lighting\n").strip().lower()
    try:
        match selection:
            case "1" | "paint":
                area = input('Please input values in forms of "1x2": ').replace(" ", "").split("x")
                area = float(input("How many walls are you painting? ")) * float(area[0]) * float(area[1])
                cans = (area/x)
                print(f"You will need {cans} cans of paint which cost $25 each. \nYour total cost will be {cans*25}.\n")
            case "2" | "flooring": pass
            case "3" | "lighting": pass
    except IndexError: print("You provided invalid syntax")

    return(area)




main()
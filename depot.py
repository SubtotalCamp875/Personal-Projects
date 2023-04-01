import math

def main():
    selection = input(f"Please select a department: \n1. Paint\n2. Flooring\n3. Lighting\nSelection: ").strip().lower()
    match selection:


        case "1" | "paint" | "one":
            try:
                length, walls = input('What is the length and width of your wall? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), float(input("How many walls will you be painting? "))
                area = walls * float(length[0]) * float(length[1])
                cans = math.ceil(area/350)
                return(print(f"\nYou will need {cans} cans of paint for {area} square inches of wall. \nEach can of paint will cost $25.00 and cover 350 square inches. \nYour total cost will be {cans*25}.00 dollars.\nYou will have {cans*350-area} square inches of paint left over.\n"))
            except IndexError: print("You provided invalid syntax.")


        case "2" | "flooring" | "two":
            try:
                length, flooring = input('What is the length and width of your floor? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), str(input("What kind of flooring would you like? (Please enter an integer)\n1. 10in. by 10in. Tiles\n2. Carpet\nSelection: ")).lower().strip()
                match flooring:
                    case "1" | "one":
                        area = int(length[0]) * int(length[1])
                        tiles = area/100
                        return(print(f"\nYou will need {tiles} of the 10in. by 10in. Tiles.\nIndividaul tiles will cost $5.00 so you would need ${tiles*5} worth of tiles. \n"))
                    case "2" | "two":
                        pass
            except IndexError: print("You provided invalid syntax.")


        case "3" | "lighting" | "three":
            pass


main()
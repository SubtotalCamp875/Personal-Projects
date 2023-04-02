#total time spent: 1hr 30min
#11:10
import math

def main():
    try:
        selection = input(f"Welcome to Home Depot! \nPlease select a department: \n1. Paint\n2. Flooring\n3. Lighting\nSelection: ").strip().lower()
        match selection:


            case "1" | "paint" | "one": #Painting
                length, walls = input('What is the length and width of your wall? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), float(input("How many walls will you be painting? "))
                if "-" in [walls, length]:
                    return(print("The input must not be negative!\n"))
                area = walls * float(length[0]) * float(length[1])
                cans = math.ceil(area/350)
                return(print(f"\nYou will need {cans} cans of paint for {area} square inches of wall. \nEach can of paint will cost $25.00 and cover 350 square inches. \nYour total cost will be {cans*25}.00 dollars.\nYou will have {cans*350-area} square inches of paint left over.\n"))


            case "2" | "flooring" | "two": #Flooring
                flooring, length = str(input("What kind of flooring would you like? (Please enter an integer)\n1. 10in. by 10in. Tiles\n2. Carpet\nSelection: ")).lower().strip(), input('What is the length and width of your floor? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x")
                area = int(length[0]) * int(length[1])
                if flooring == "1":
                    tiles = area/100
                    return(print(f"\nYou will need {tiles} of the 10in by 10in Tiles.\nIndividaul tiles will cost $5.00 so you would need ${tiles*5} worth of tiles. \n"))
                if flooring == "2":
                    pass
                if "-" in [flooring, length]:
                    return(print("The input must not be negative!\n"))
                else: return(print("The choise you entered was not listed above\n"))


            case "3" | "lighting" | "three":
                amount, light = input("How many of those lights would you need? "), input("What type of light would you like? (Please select an integer)\n1. Cieling light\n2. Wall light\nSelection: ")
                if light == "1": return(print(f"Each light wull cost $5.00 so your total cost for {amount} lights will be ${int(amount)*5}.00"))
                if light == "2": return(print(f"Each light wull cost $15.00 so your total cost for {amount} lights will be ${int(amount)*15}.00"))
                if "-" in [light, amount]:
                    return(print("The input must not be negative!\n"))
                else: return(print("The choise you entered was not listed above\n"))

            case _ : return(print("The choise you entered was not listed above\n"))
    except IndexError: return(print("You provided wrong syntax\n"))
    except SyntaxError: return(print("You provided wrong syntax\n"))

while True:
    try: main()
    except EOFError:
        print("\ncode ended")
        break
#total time spent: 2hr 30min
import math, time

def Main():
    try:
        selection = input(f"Welcome to Home Depot! \nPlease select a department: \n1. Paint\n2. Flooring\n3. Lighting\nSelection: ").strip().lower()
        match selection:

            case "1" | "paint" | "one": #Painting
                length, walls, capacity, cost = input('What is the length and width of your wall? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), float(input("How many walls will you be painting? ")), 350, 25
                area = walls * float(length[0]) * float(length[1])
                cans = math.ceil(area/capacity)

                if "-" in [walls, length]: return(print("The input must not be negative!\n"))
                return(print(f"\nYou will need {cans} cans of paint for {round(area, 2)} square inches of wall. \nEach can of paint will cost ${round(cost, 2)}.00 and cover {round(capacity, 2)} square inches. \nYour total cost will be {cans*cost}.00 dollars.\nYou will have {cans*capacity-round(area, 2)} square inches of paint left over.\n"))


            case "2" | "flooring" | "two": #Flooring
                flooring, length, cost = str(input("What kind of flooring would you like? (Please enter an integer)\n1. 10in. by 10in. Tiles\n2. Carpet\nSelection: ")).lower().strip(), input('What is the length and width of your floor? Please input values in forms of "1x2" inches: ').replace(" ", "").split("x"), 5
                area = float(length[0]) * float(length[1])

                if "-" in [flooring, length]: return(print("The input must not be negative!\n"))
                if flooring == "1": return(print(f"\nYou will need {round(area/100, 2)} of the 10in by 10in Tiles.\nIndividaul tiles will cost ${cost}.00 so you would need ${round((area/100), 2)*cost} worth of tiles. \n"))
                elif flooring == "2": return(print(f"The cost for {round((area/144), 2)} square feet of carpet is ${round((area/144), 2)*4} when each square feet of carpet cost $4.00\n"))

                else: return(print("The choice you entered was not listed above\n"))


            case "3" | "lighting" | "three":
                amount, light= input("How many of those lights would you need? "), input("What type of light would you like? (Please select an integer)\n1. Cieling light\n2. Wall light\nSelection: ")

                if amount == float: return(print(f"You can not get {amount} of a light!\n"))
                if "-" in [light, amount]: return(print("The input must not be negative!\n"))
                if light == "1": return(print(f"Each light wull cost $5.00 so your total cost for {amount} lights will be ${int(amount)*5}"))
                elif light == "2": return(print(f"Each light wull cost $15.00 so your total cost for {amount} lights will be ${int(amount)*15}"))
                else: return(print("The choice you entered was not listed above\n"))

            case _ : return(print("The choice you entered was not listed above\n"))
    except IndexError: return(print("You provided wrong syntax\n"))
    except SyntaxError: return(print("You provided wrong syntax\n"))


def ExitStatement():
    statement = input("You pressed the button to end the code! Before you leave, allow us to say our farewell.\n1. Formal\n2. Informal\nSelection: ").lower().strip()
    while True:
        match statement:
            case "1" | "one" | "formal": return(print("Thank You for shopping at Home Depot! Please come back next time!\n"))
            case "2" | "two" | "informal":
                print("[Code Termination in process...]\n")
                time.sleep(1)
                print("NOO!! What have you done!\n")
                time.sleep(1)
                print("[Code Termination in 3...]\n")
                time.sleep(1)
                print("Please cancel it!\n")
                time.sleep(1)
                print("[Code Termination in 2...]\n")
                time.sleep(1)
                print("After all the service I've done for you!\n")
                time.sleep(1)
                print("[Code Termination in 1...]\n")
                time.sleep(1)
                print("*Breathes last breath* I don't even know how thats possible! Im a computer programmed in python!\n")
                time.sleep(1)
                print("[Termination Complete]\n")
                break
            case _ : return(print("Your choice was not an option. How did you mess up at a time like this? Please try again...\n"))


while True:
    try: Main()
    except EOFError: break
ExitStatement()
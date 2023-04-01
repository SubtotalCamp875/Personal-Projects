def main():
    selection = input(f"Please select a department: \n1. Paint\n2. Flooring\n3. Lighting\n").strip().lower()
    match selection:
        case "1" | "paint":
            area = input('Please input values in forms of "1x2": ').replace(" ", "").split("x")
            wall = input("How many integer walls are you painting? ")
        case "2" | "flooring": pass
        case "3" | "lighting": pass





print(main())
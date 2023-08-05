from colorama import Fore
import time

def main():
    skip = False
    while True:
        if skip == False:
            func = int(input('Graph maker (1), Graph Shifting (2), Syntax Pairing (3), Coordinate Pairs (4), Conversion (5), Differences (6), Help/Explanation (7): '))
            answer, current = "y_{ 1}=".replace(' ',''), 0
            steps, notes_list  = ['0','1','2','3','4','5','6','7','8','9','10','11','12'], ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e2']
            notes = dict(zip(notes_list,steps))
        skip = False

        match func:
            case 1: #Graph Maker
                values = input('Input values for n and t (ex. [n t,-n t.0] [5 6,a 10.5] or visit Syntax Pairing by inputing "v"): ').replace('[','').replace(']','').split(',')

                if values[0] == 'v':
                    skip, func = True, 'v'
                    print('Switching to Syntax pairing (2) now...\n')
                    continue

                for i in range(len(values)):
                    values[i] = values[i].split(' ')
                    if values[i][0].lower() not in notes_list: current += int(values[i][0])

                    #replace notes with number in 2d array
                    if values[i][0].lower() in notes_list:
                        values[i][0] = notes[values[i][0].lower()]
                        #find difference between prev value and notes when notes is not the first value
                        if i > 0:
                            values[i][0] = int(values[i][0]) - current
                            current += int(values[i][0])
                    answer += f'+g\left(x,{values[i][0]},{values[i][1]}\ right)'.replace(' ','')

                print(f'\n{answer}\n')
                print(('g\left(x,n,t\ '+'right)\ =\ \ '+'frac{n}{1+e^{60\left(-x+t\ '+'right)}}\n').replace(' r','r').replace(' f','f'))

            case 2:
                values, x, y = input('Input values for n and t (ex. [n t,-n t.0] [5 6,a 10.5] or visit Syntax Pairing by inputing "v"): ').replace('[','').replace(']','').split(','), 0, 1
                if values[0] == 'v':
                    skip, func = True, 'v'
                    print('Switching to Syntax pairing (2) now...\n')
                    continue
                change_amount, shift = input('How much should the graph shift by (ex. [y=5, x=-3] [y=10, x=8])? ').replace('[','').replace(']','').replace('x=', '').replace('y=', '').replace(' ','').split(','), input('What coord should the shift start on (ex. y=3, x=7)? ').replace('[','').replace(']','').replace('x=', '').replace('y=', '').replace(' ','').split(',')

                for i in range(len(values)):
                    values[i] = values[i].split(' ')
                    if values[i][0].lower() not in notes_list: current += int(values[i][0])

                    #replace notes with number in 2d array
                    if values[i][0].lower() in notes_list:
                        values[i][0] = notes[values[i][0].lower()]
                        #find difference between prev value and notes when notes is not the first value
                        if i > 0:
                            values[i][0] = int(values[i][0]) - current
                            current += int(values[i][0])
                    if i+1 >= int(shift[x]): values[i][x] = int(values[i][x]) + int(change_amount[x])
                    if i+1 >= int(shift[y]): values[i][y] = float(values[i][y]) + float(change_amount[y])
                    answer += f'+g\left(x,{values[i][x]},{values[i][y]}\ right)'.replace(' ','')

                print(f'\n{answer}\n')
                print(('g\left(x,n,t\ '+'right)\ =\ \ '+'frac{n}{1+e^{60\left(-x+t\ '+'right)}}\n').replace(' r','r').replace(' f','f'))


            case 3 | 'v': #Syntax Pairing
                pair, x, y = '', input('Enter list of First value (1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
                for i in range(len(x)): pair += f'{x[i]} {y[i]},'
                print(pair[0:-1])


            case 4: #Coordinate Pairs
                pair, x, y = '', input('Enter list of First value (ex. 1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
                for i in range(len(x)): print(f'{x[i]}, {y[i]}')


            case 5: #Conversions
                values = input('Enter a list of values (ex. 1,2,d#,e,5): ')
                print(f'\n{convert(values, "l")}\n{convert(values, "n")}\n')


            case 6: #Differences
                print(difference(convert(input('Enter list of values (ex. 1,2,d#,e,5): ').lower(), 'n').replace(' ','').split(',')))

            case 7:
                print(Fore.GREEN+'\nAbout this project - The first version of this project was created when I, SubtotalCamp875, along with YackaDesmos wanted to create a Rickroll using Desmos Graphing Calculator. I then created this project to further optimize the code and features as it was easier to rewrite the code compared to modifying its whole i/o and syntax system. We also created our own discord server with the help of Playli750! The system also surports notes like a,a#,b,...,g,g# (calculated by Yacka). Note that the code is not perfect and might contain bugs and also requires the user to use the correct syntax or else it will raise an error. If you find any bugs or would like to discuss anything, Join the Discord Server!\n'+Fore.YELLOW+'The Original Video by SubtotalCamp875: '+Fore.BLUE+'https://youtu.be/JtP_3Jao910 \n'+Fore.YELLOW+'YackaDesmos Channel: '+Fore.BLUE+'https://www.youtube.com/@YackalipsDesmos/about \n'+Fore.YELLOW+'Playli750 channel: '+Fore.BLUE+'https://www.youtube.com/@playli750/about \n'+Fore.YELLOW+'The Desmos Graphing Server (Discord): '+Fore.BLUE+'https://discord.gg/rQrnMtJmsv \n')

                time.sleep(2)
                print(Fore.GREEN+'Mode 1 - The first mode, also the main mode, requires the syntax [n t,-n t.0] [5 6,a 10.5] where the n value has 2 options (the change in height at the location or setting the hieght at the note) for t (on the x coordinate). The input can be numbers, notes, negetives numbers, or all the above. However it can not be a negetive note. When the input is a pos/neg whole number, it will +/- that number from the previous value BUT if the input is a note, then the hieght will the SET to that note. (see note scale here: '+Fore.BLUE+'https://www.desmos.com/calculator/mnejx8fjc2)\n'+Fore.YELLOW+'So if n=5 and t=6, there will be a increase of 5 in height from (6,0) to (6,5) on a graph making it look like a backwards "L".\n'+Fore.RED+'The next set of numbers (seperated by the comma) increased at the next given x coordinate (t) but increase/decrease based in the previous value of 5.\n'+Fore.WHITE+'The mode also supports "v" which will automatically bring you to Mode 3 to help you create the syntax.\n')

                time.sleep(2)
                print(Fore.GREEN+'Mode 2 - Mode 2 is the same as Mode 1 in the sense that is ask you for the same inputs as Mode 1 and also supports an input of "v" but its main purpose is to shift the graph by a certain amount.\n'+Fore.YELLOW+'When asked the second question (How much should the graph shift by?) you are required to enter in the syntax of "y=5, x=-3" or "y=10, x=8" where it can be any number or note. The amount stated will be the amount the pionts on the graph shift by. If there was a piont at (1,0) and "y=3, x=0" then the result will be (4,0).\n'+Fore.RED+'The third questions (What coord should the shift start on?) requires the same syntax as question 2 BUT this time, the numbers define where the change in starting. The numbers are based on the pionts you gave and not the location on a graph. If you inputted pionts on (5,0), (6,5), (7,3), then if y=1, the change in x will start at (5,0) and also increases the x value of all pionts after.\n'+Fore.WHITE+'The mode also supports "v" which will automatically bring you to Mode 3 to help you create the syntax.\n')

                time.sleep(2)
                print(Fore.GREEN+'Mode 3 - You can acess mode 3 by typing "v" as the input of the first question in both mode 1 and 2. The input requires a set of values seperated by commas (1,2,3,4,5) and can be numbers or notes. The second input must be the same length as the first.\n'+Fore.YELLOW+'The first list value is the variable n within the equation and the second inputted list of values represent variable t. The result of the pairing will result in the correct syntax that is required for mode 1 and 2.\n'+Fore.RESET)

                time.sleep(2)
                print(Fore.GREEN+'Mode 4 - The syntax for mode 4 is the same as mode 3 but instead of pairing them in the syntax for mode 1 and 2, it pairs them in the normal coordinate pairs where the first value of the first input is paired and seperated by a comma with the first value of the second input.\n'+Fore.RESET)

                time.sleep(2)
                print(Fore.GREEN+'Mode 5 - The input of mode 5 can be any number or note seperated by the comma and will output both the list of values in number and notes.\n'+Fore.RESET)

                time.sleep(2)
                print(Fore.GREEN+'Mode 6 - The syntax is the same as mode 5 but its output will be the difference between the values and the value before it. The first value will always stay the same as there is no value before it.\n'+Fore.RESET)

                time.sleep(2)
                print(Fore.GREEN+'Mode 7 - The most usful mode and also the easiest to use. It gives all the diffinition and explaination of all other modes in words that are clear or not. It has no inputs but sends the largest output. It takes 14 seconds for the entirety of the text to print even though it could take just 1. And becuase of the time and coloring effects, the code gained an extra 21 lines when it could be all printed using 1 line\n'+Fore.RESET)

def convert(values, mode):
    steps, notes_list  = ['0','1','2','3','4','5','6','7','8','9','10','11','12'], ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e2']
    notes, numbers = dict(zip(notes_list,steps)), dict(zip(steps,notes_list))
    values = values.replace(' ','').split(',')
    numbers_list, letters_list = '', ''

    for i in range(len(values)):
        #turns number to letter if i is number and add number to number list
        if values[i] in steps:
            letters_list += f'{numbers[values[i]]}, '
            numbers_list += f'{values[i]}, '
        #turns letter to number if i is letter and add letter to letter list
        if values[i].lower() in notes_list:
            numbers_list += f'{notes[values[i].lower()]}, '
            letters_list += f'{values[i].lower()}, '

    if mode == 'l': return(letters_list[0:-2])
    if mode == 'n': return(numbers_list[0:-2])



def difference(values):
    difference = ''
    for i in range(len(values)):
        if i == 0: difference += f'{values[i]}, '
        if i != 0: difference += f'{int(values[i]) - int(values[i-1])}, '
    return(difference[0:-2])


if __name__ == '__main__':
    main()
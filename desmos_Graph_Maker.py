def main():
    func = int(input('Graph maker = 1, Syntax Pairing = 2, Coordinate Pairs = 3, Conversion = 4, Differences = 5, Help/Explanation = : '))
    answer = "y_{ 1}=".replace(' ','')
    steps, notes_list  = ['10','11','12','13','1','2','3','4','5','6','7','8','9'], ['a', 'a#', 'b', 'b#', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    notes = dict(zip(notes_list,steps))

    match func:
        case 1: #Graph Maker
            values = input('Input values for n and t (ex. [n t,-n -t] [5 6,-a -10] or visit Syntax Pairing): ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(' ')
                #replace notes with number in 2d array
                if values[i][0].lower() in notes_list:
                    values[i][0] = notes[values[i][0].lower()]
                    #find difference between prev value and notes when notes is not the first value
                    if i > 0: values[i][0] = int(values[i][0]) - int(values[i-1][0])
                answer += f'+g\left(x,{values[i][0]},{values[i][1]}\ right)'.replace(' ','')
            print(f'\n{answer}\n')
            print(('g\left(x,n,t\ '+'right)\ =\ \ '+'frac{n}{1+e^{60\left(-x+t\ '+'right)}}\n').replace(' r','r').replace(' f','f'))

        case 2: #Syntax Pairing
            pair, x, y = '', input('Enter list of First value (1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
            for i in range(len(x)): pair += f'{x[i]} {y[i]},'
            print(pair[0:-1])

        case 3: #Coordinate Pairs
            pair, x, y = '', input('Enter list of First value (ex. 1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
            for i in range(len(x)): print(f'{x[i]}, {y[i]}')

        case 4: #Conversions
            values = input('Enter a list of values (ex. 1,2,d#,e,5): ')
            print(f'\n{convert(values, "l")}\n{convert(values, "n")}\n')

        case 5: #Differences
            print(difference(convert(input('Enter list of values (ex. 1,2,d#,e,5): ').lower(), 'n').replace(' ','').split(',')))



def convert(values, mode):
    steps, notes_list  = ['10','11','12','13','1','2','3','4','5','6','7','8','9'], ['a', 'a#', 'b', 'b#', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
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
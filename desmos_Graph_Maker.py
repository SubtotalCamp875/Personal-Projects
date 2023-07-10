def main():
    func = int(input('Graph maker = 1, Syntax Pairing = 2, Coordinate Pairs = 3, Conversion = 4, Help/Explanation = : '))
    answer = "y_{ 1}=".replace(' ','')
    steps, notes_list  = ['10','11','12','13','1','2','3','4','5','6','7','8','9'], ['a', 'a#', 'b', 'b#', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    notes, numbers = dict(zip(notes_list,steps)), dict(zip(steps,notes_list))

    match func:
        case 1:
            values = input('Input values for n and t (ex. [n t,-n -t] [5 6,-a, 10] or visit Syntax Pairing): ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(' ')
                #replace notes with number
                if values[i][0].lower() in notes_list:
                    values[i][0] = notes[values[i][0].lower()]
                    #find difference between prev value and notes when notes is not the first value
                    if i > 0: values[i][0] = int(values[i][0]) - int(values[i-1][0])
                answer += f'+g\left(x,{values[i][0]},{values[i][1]}\ right)'.replace(' ','')
            print(f'\n{answer}\n')
            print(('g\left(x,n,t\ '+'right)\ =\ \ '+'frac{n}{1+e^{60\left(-x+t\ '+'right)}}\n').replace(' r','r').replace(' f','f'))

        case 2:
            pair, x, y = '', input('Enter list of First value (1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
            for i in range(len(x)): pair += f'{x[i]} {y[i]},'
            print(pair[0:-1])

        case 3:
            pair, x, y = '', input('Enter list of First value (ex. 1,2,3,4,5): ').replace(' ','').split(','), input('Enter list of Second value (ex. 1,2,3,4,5): ').replace(' ','').split(',')
            for i in range(len(x)): print(f'{x[i]}, {y[i]}')

        case 4:
            values = input('Enter a list of values (ex. 1,2,d,e#,5): ').replace(' ','').split(',')
            mode = input('Convert all to Letters (L) or Numbers (N)? ')
            if mode == 'L':
                for i in range(len(values)):
                    values[i] = numbers[values[i]]
            print(values)






if __name__ == '__main__':
    main()
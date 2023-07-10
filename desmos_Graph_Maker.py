def main():
    func = int(input('Graph maker = 1, Pairing = 2, Help/Explanation = 3: '))
    answer = "y_{ 1}=".replace(' ','')
    steps, notes_list  = ['10','11','12','13','1','2','3','4','5','6','7','8','9'], ['a', 'a#', 'b', 'b#', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    notes = dict(zip(notes_list,steps))

    match func:
        case 1:
            values = input('Input n and t in forms of "n t,-n -t" etc: ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(' ')
                #replace notes with number
                if values[i][0] in notes_list:
                    values[i][0] = notes[values[i][0]]
                    #find difference between prev value and notes when notes is not the first value
                    if i > 0: values[i][0] = int(values[i][0]) - int(values[i-1][0])
                answer += f'+g\left(x,{values[i][0]},{values[i][1]}\ right)'.replace(' ','')
            print(f'\n{answer}\n')

        case 2: pass
        case 3: pass

if __name__ == '__main__':
    main()
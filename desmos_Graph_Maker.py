def main():
    func = int(input('Graph maker = 1, Help/Explanation = 2: '))
    answer = ""
    match func:
        case 1:
            values = input('Input n and t in forms of "n:t,n:t" etc: ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(':')
            for i in range(len(values)):
                answer += f'+g\left(x,{values[i][0]},{values[i][1]}\ right)'.replace(' ','')
            print(answer)


        case 2: pass





if __name__ == '__main__':
    main()
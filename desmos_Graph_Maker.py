def main():
    func = input('Graph maker: 1, Help/Explanation: 2')
    answer = ""
    match func:
        case 1:
            values = input('Input n and t in forms of "n:t,n:t" etc: ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(':')
            for i in range(len(values)):
                answer += f'+g\left(x,{values[i][0]},{values[i][1]}\right)'



        case 2:





if __name__ == '__main__':
    main()
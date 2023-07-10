def main():
    func = input('Graph maker: 1, Help/Explanation: 2')

    match func:
        case 1:
            values = input('Input n and t in forms of "n:t,n:t" etc: ').split(',')
            for i in range(len(values)):
                values[i] = values[i].split(':')
            


        case 2:





if __name__ == '__main__':
    main()
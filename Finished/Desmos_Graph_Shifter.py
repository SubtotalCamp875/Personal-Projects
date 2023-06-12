def main():

    func = int(input('1 = Coordinate Pairs, 2 = Shift Horizontal, 3 = Create W. Notes, 4 = Help: '))
    steps, notes_list  = ['10','11','12','13','1','2','3','4','5','6','7','8','9'], ['a', 'a#', 'b', 'b#', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    notes = dict(zip(notes_list,steps))

    match func:
        case 1:
            sign, a, b = request_input()
            sign = sign_list(sign)
            for i in range(len(a)): print(f'{sign[i]}{a[i]},{b[i]}')

        case 2:
            sign, sign_dummy, a, a_dummy, b = request_input()
            sign = sign_list(sign)
            unchanged, adder, b_dummy = int(input('How many do you want unchanged: ')), float(input('How much do you want to shift (+x/-x): ')), ''
            print('\ny_{1}=',end='')

            for i in range(unchanged):
                print(f'{sign[i]}g\left(x,{a[i]},{b[i]}\ right)'.replace(' ',''),end = '')
                b_dummy += f'{b[i]},'

            for i in range(len(a)-unchanged):
                i += unchanged
                print(f'{sign[i]}g\left(x,{a[i]},{float(b[i])+adder}\ right)'.replace(' ','').replace('.0',''),end = '')
                b_dummy += f'{float(b[i])+adder},'

            print(('\ng\left(x,n,t\ '+'right)\ =\ \ '+'frac{n}{1+e^{60\left(-x+.5t\ '+'right)}}').replace(' r','r').replace(' f','f'))
            print(f'\n{sign_dummy}\n\n{a_dummy}\n\n{b_dummy[:-1].replace(".0","")}')

        case 3:
            sign, a, a_dummy = '1', [], str(input('Input notes (ex. a,b,c,d): ')).lower().replace(' ','').split(',')
            for i in range(len(a_dummy)):

                #converts a-z >> #
                if a_dummy[i] in notes_list: a.append(float(notes[a_dummy[i]]))
                else: return(print('please input notes'))

                #find differnce between value and prev value
                if i == 0: continue
                else:
                    a[i] = float(notes[a_dummy[i-1]])-a[i]
                    if a[i] == -abs(a[i]):
                        a[i] = abs(a[i])
                        sign += '1'
                    else: sign += '0'
            print(f"The difference in value is {str(a).replace('.0', '')} and sign = {sign}")
    print(' ')

        case 4:
            print("Make sure you are providing the correct syntax (some require commas, some don't) and capitalization (lower case) there must be the same amount of charaters for sign, height, AND distance.\n")
            print('Link to graph: https://www.desmos.com/calculator/wsxy6t0fcr')
            print('Desmos graph size settings: 0<y<12  -3<x<62')
            print('sign = 110110011011000011011000110011011001101010011011000110 \n height = 2,3,3,7,1,3,7,2,3,3,5,1,3,1,2,2,2,3,3,3,2,3,2,2,2,5,2,5,2,3,3,7,1,3,7,2,3,3,10,8,1,1,4,2,3,3,3,2,3,2,2,2,5,2 \n distance = 1,2,3,4,6.5,10,15,16,17,18,19,21,24,26,27,28.8,30,31,32,33,36,38,40.5,41.5,44,46,50,55,57,58,59,60,62,66,70.5,71.5,72.5,73.5,74.5,77.5,79.5,82.5,83.5,85.5,86.5,87.5,88.5,91.5,93.5,96.5,97.5,101.5,102.5,106.5\n')
            print('Credit: SubtotalCamp875 - https://github.com/SubtotalCamp875/Personal-Projects/tree/c77eed059c5f0be235725981f0aa0e64b67b6a79/Finished\n')




def request_input():
    sign_dummy, a_dummy, b = input('Sign (1=+, 0=-)(ex. 10110): '), str(input('Input the change in height (ex. 1,1,2,5): ')).replace(' ',''), str(input('Input of distance (ex. 2,5,8): ')).replace(' ','').split(',')
    sign, a = list(sign_dummy), a_dummy.split(',')
    return(sign, sign_dummy, a, a_dummy, b)


def sign_list(sign):
    sign_dummy = []
    for i in range(len(sign)):
        sign_dummy.append(sign_assign(sign,i))
    return(sign_dummy)


def sign_assign(sign,i):
    if sign[i] == '1': return('+')
    if sign[i] == '0': return('-')

if __name__ == '__main__':
    main()

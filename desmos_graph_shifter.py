def main():

    func = int(input('1 = Coordinate Pairs, 2 = Shift Horizontal, 3 = Create W. Notes: '))
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
            unchanged, adder, b_dummy = int(input('How many do you want unchanged: ')), int(input('How much do you want to shift (+x/-x): ')), ''
            print('\ny_{1}=',end='')

            for i in range(unchanged):
                print(f'{sign[i]}g\left(x,{a[i]},{b[i]}\ right)'.replace(' ',''),end = '')
                b_dummy += f'{b[i]},'

            for i in range(len(a)-unchanged):
                i += unchanged
                print(f'{sign[i]}g\left(x,{a[i]},{float(b[i])+adder}\ right)'.replace(' ','').replace('.0',''),end = '')
                b_dummy += f'{float(b[i])+adder}, '

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


def request_input():
    sign_dummy, a_dummy, b = input('Sign (1=+, 0=-)(ex. 10110): '), str(input('Input of change in height (ex. 1,1,2,5): ')).replace(' ',''), str(input('Input of distance (ex. 2,5,8): ')).replace(' ','').split(',')
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
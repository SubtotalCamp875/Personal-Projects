
x = [
'+g\left(x,7,1\right)',
'+g\left(x,5,1.75\right)',
'-g\left(x,1,2\right)',
'-g\left(x,2,2.5\right)',
'+g\left(x,5,3\right)',
'-g\left(x,3,3.5\right)',
'-g\left(x,4,4.25\right)',
'-g\left(x,5,4.5\right)',
'+g\left(x,12,5\right)',
'-g\left(x,5,5.75\right)',
'+g\left(x,2,6\right)',
'+g\left(x,1,6.5\right)',
'-g\left(x,1,7\right)',
'-g\left(x,4,7.5\right)',
'-g\left(x,5,8\right)',
'+g\left(x,10,8.5\right)',
'-g\left(x,5,9\right)',
'+g\left(x,5,9.75\right)',
'-g\left(x,1,10\right)',
'-g\left(x,2,10.5\right)',
'+g\left(x,5,11\right)',
'-g\left(x,3,11.5\right)',
'-g\left(x,4,12.25\right)',
'-g\left(x,5,12.75\right)',
'+g\left(x,5,13\right)',
'+g\left(x,5,13.75\right)',
'-g\left(x,1,14\right)',
'-g\left(x,2,14.5\right)',
'+g\left(x,5,15\right)',
'-g\left(x,3,15.5\right)',
'-g\left(x,1,16\right)',
'-g\left(x,3,16.5\right)\left\{x>H_{halfMark}\right\}',
'+g\left(x,7,17.5\right)',
'-g\left(x,5,18\right)',
'+g\left(x,2,18.5\right)',
'+g\left(x,3,18.75\right)',
'-g\left(x,5,20\right)',
'+g\left(x,3,21.25\right)\left\{x<11.01,11.15<x\right\}',
'-g\left(x,2,22.5\right)',
'-g\left(x,3,23.25\right)',
'+g\left(x,7,23.75\right)\left\{x<12.1,12.2<x\right\}',
'-g\left(x,7,24.5\right)',
'+g\left(x,7,25.5\right)',
'-g\left(x,5,26\right)',
'+g\left(x,2,26.5\right)',
'+g\left(x,3,26.75\right)',
'-g\left(x,5,28\right)',
'+g\left(x,3,29.25\right)\left\{x<15.01,15.15<x\right\}',
'-g\left(x,2,30.5\right)',
'-g\left(x,3,31.25\right)',
'+g\left(x,7,32.75\right)\left\{x<16.7,16.85<x\right\}',
'-g\left(x,7,34\right)',
]
l = []
for i in range(len(x)):
    l.append(x[i].replace(f"g\left(x,", '').replace("\right)", ''))

for i in range(len(l)):
    print(f"'{l[i]}',")

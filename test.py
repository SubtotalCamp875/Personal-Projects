s_straights_list = [['1','2','3','4'],['2','3','4','5'],['3','4','5','6']]
dice = ['1','2','3','4','4']
print(dice)


for i in range(3):
    if str(s_straights_list[i]).replace('[','').replace(']','') in str(dice): print('Small straight for: 30\n')
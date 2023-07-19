import random

dice, reroll = [random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1, random.choice(range(6))+1], 2
print(dice)
dice.sort()
print(dice)
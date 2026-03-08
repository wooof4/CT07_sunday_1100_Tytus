import random
round=0
Health=100
print('Hero starts on his adventure with Health: 100')
while not Health<=0:
    damage=random.randint(1,15)
    Health=Health-damage
    print('After fighting monsters, his Health is now:'+str(Health) )
    round=round+1
print('your hero is dead')
print('After fighting monsters, his Health is now: 0 He fought '+str(round)+' battles, and died.')

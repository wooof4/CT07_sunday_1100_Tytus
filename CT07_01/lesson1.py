print("Hello from lesson 1")
#make variable (typeofrubbish)
#import random
#a=random.randint(1,3)
#if a==1: typeofrubbish='glass'
#if a==2: typeofrubbish='plastic'
#if a==3: typeofrubbish='paper'
#if typeofrubbish='glass':print('into glass bin')
#if typeofrubbish='plastic':('into plastic bin')
#if typeofrubbish='paper':('into paper bin')
# red=1
# blue=2
# yellow=3
# no_red=red*3
# no_blue=blue*5
# no_yellow=yellow*4
# print(str(no_red+no_blue+no_yellow))
# score_one = 80
# score_two = 90
# score_three = 75
# total = int(score_one) + int(score_two) + int(score_three)
# average_score = int(total / 3)
# student_name = "Alex"
# print("Average score for " + student_name + " is: " + str(average_score))
score=int(input('whats ur score'))
if score>=75:
    print('grade A')
elif score>60 and score<75:
    print('grade B')
elif score>50 and score<60:
    print('grade C') 
else:
    print('fail')
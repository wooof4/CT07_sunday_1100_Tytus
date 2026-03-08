# print("Hello from lesson 3")
# while True:
#     answer=input("the alphabet from a-z but i go from z-a what am i")
#     if answer=='zebra':
#         print('correct')
#         break
# a=10
# while True:
#     print(str(a))
#     a=a-1
#     if a==-1:
#         print('gud job')
#         break
# savings=int(input('how much would save everyday'))
# money=0
# while True:
#     money=money+savings
#     print('$'+str(money))
#     if money>=100:
#         print('money over 100')
#         break
# import random
# chances=3
# correct=0
# while True:
#     num1=random.randint(1,20)
#     num2=random.randint(1,20)
#     question=int(input(str(num1)+'*'+str(num2) + ' '))
#     if question==int(num1)*int(num2):
#         correct=correct+1
#         print(str(correct))
#     else:
#         chances=chances-1
#     if chances==0:
#         print('see me in my office')
#         break
#     if correct==20:
#         break
import datetime
print(datetime.datetime.now())

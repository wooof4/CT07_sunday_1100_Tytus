# print("Hello from lesson 4")
##recap 1##
# countdown=10
# while True:
#     print(str(countdown))
#     countdown=countdown-1
#     if countdown==0:
#         print('HAPPY NEW YER')
#          break

##task 1##
import random
# coinflip=random.randint(1,2)
# planet=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# print('I have conquered '+ planet[3])
# planet[3]='goog'
# print(planet[3]+" has launced war against earth ")
# if coinflip==1:
#     print('earth has won against goog')
# elif coinflip==2:
#     print('goog has won against earth')

##task 2##
# planet=['Mercury', 'Venus', 'Earth', 'Mars', 
# 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# planet.append('goog')
# for item in planet:
#     print(item)
#     if item=='Earth':
#         print('my home')
#     if item=='Mars':
#         print('conquered by my balls')
#     if item=='goog':
#         print('i created this planet')

##task 3##
# countries=[]
# while True:
#     a=input('what country would u like to visit ')
#     countries.append(a)
#     if a=='end':
#         for item in countries:
#             print ('i would like to go to '+ countries[item])
#             break
##task 4##
menu=[]
while True:
    food=input('what food should we put in the menu')
    menu.append(food)
    if food=='end':
        print(menu)
        break
print('oh look a customer a come in')
ordered=[]
order=''
while not order=='end':
    order=input('what food would u like to eat '+ str(menu))
    ordered.append(order)
print(ordered)
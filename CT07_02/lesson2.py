# print("Hello from lesson 2")
# for i in range(2,25,2):
#     print(str(i))
# for i in range(0,21):
#     print(str(i))
# for a in range(1,31):
#     print(str(a))
# i=2
# while i<=9:
#     print(str(i))
#     if i==5:
#         break
#     else:
#         print(str(i))
#         i=i+1
# pizza='dough,cheese,tomato'
# while True:
#     topping=input('wat topping would on pizza ')
#     pizza=pizza+','+topping
#     if topping=='end':
#         print(pizza)
#         break
trys=0
while True:
    question_1=input('how many tires are there on a car')
    if question_1=='4':
        question_2=input('how many times does garreth goon a day')
        if question_2=='10':
            question_3=input('how  many times has the wifi crashed')
            if question_3=='100':
                print(str(trys)+' trys')
                if trys>=3:
                    print('u lose')
                    break
                else:
                    print('u win')
                    break
            else:
                trys=trys+1
        else:
            trys=trys+1
    else:
        trys=trys+1
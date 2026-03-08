order=[]

while True:
    food=input('what would you like to order?')
    i=0
    if food=='end':
        for items in order:
            i=i+1
            print(str(i)+ '. ' + items)            
        break
    else:
        order.append(food)
        
        for items in order:
            i=i+1
            print(str(i)+ '. ' + items)
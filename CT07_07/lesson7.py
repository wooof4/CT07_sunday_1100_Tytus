print("Hello from lesson 7")
# students=[]
# student1=['Brandon','83334192','Enterprise']
# Student2=['Rayden','65394082','npcc',]
# student3=['Thomas','97974782','npcc']
# students.append(student1)
# students.append(Student2)
# students.append(student3)
# print(students)
# for student in students:
#     name,phonenum,cca=student
#     print('name:'+name)
#     print('phonenum:'+phonenum)
#     print('CCA:'+ cca)

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]
# list3=list1+list2
# print(list3)

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]
# list3=list1+list2
# sorted_list=sorted(list3)
# print(sorted_list)

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3
# sliced=fruits[:index]
# sliced2=fruits[3:6]
# print(sliced)
# print(sliced2)
common=[]
list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

for item in list1:
    if item in list2:
        common.append(item)
    print(common)
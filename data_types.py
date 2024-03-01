# Create an empty list called my_list
my_list = []

#append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# print the updated list
print(my_list)

#insert the value 15 at the second position in the list
my_list.insert(1,15)
print(my_list)

#Extend my_list with another list: [50, 60, 70]
my_list.extend([50,60,70])
print(my_list)

#Remove the last element from my_list
my_list.pop(-1)
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list
element = 30
index = my_list.index(element)
print(index)
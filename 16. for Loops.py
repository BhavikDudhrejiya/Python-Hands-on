list1 = ['Bhavik', 'Akshay', 'Carry Minati', 'BB ki Vines']

for i in list1:
    print(i)

list2 = [['Bhavik',1], ['Akshay',2], ['Carry Minati',3], ['BB ki Vines',4]]

for i,j in list2:
    print(i,j)

dict1 = dict(list2)
print(dict1)

for i,j in dict1.items():
    print(i,j)
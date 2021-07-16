var1 = 6
var2 = 56
print('Enter number:')
var3 = int(input())

if var3>var2:
     print('Greater')
else:
    print('Lesser')

if var3>var2:
     print('Greater')
if var3==var2:
    print('Equal')
else:
    print('Lesser')

if var3>var2:
     print('Greater')
elif var3==var2:
    print('Equal')
else:
    print('Lesser')

list1 = [1,2,5,3,6,5,4,8,5,9,5]
if 5 in list1:
    print('Yes in list')

print(5 in list1)
print(25 in list1)

if 10 not in list1:
    print('Yes not in')
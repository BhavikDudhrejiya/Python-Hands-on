#Operators in python
"""
1. Arithmetic
2. Assignment
3. Comparison
4. Logical
5. Identity
6. Membership
7. Bitwise
"""

# 1. Arithmetic
print(5+6) #Addition
print(5-6) #Subtraction
print(5*6) #Multiplication
print(15/6) #Division
print(15//6) #Floor division
print(5**6) #Exponential
print(15%6) #Reminder/Modulus

# 2. Assignment
x = 5
print(x)
x+=7
#x-=8
#x/=9
#x%=7
print(x)

# 3. Comparison
i = 8
print(i==5) #Equals to
print(i!=5) #Not Equals to
print(i<5) #Less than
print(i<=5) #Less than or Equals to
print(i>5) #Greater than
print(i>=5) #Greater than or Equals to

# 4. Logical
a = True
b = False
print(a and b)
print(a or b)

x = True
y = True
print(x and y)
print(x or y)

# 5. Identity = is or is not
a = True
b = False
print(a is b)
print(a is not b)

# 6. Membership
list1 = [3,3,2,2,39,33,35,32]
print(324 not in list1)
print(3 in list1)

# 7. Bitwise
0 - 00
1 - 01
2 - 10
3 - 11
print(0 | 3)
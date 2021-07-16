#Tuple is immutable i.e. We can not change the tuple or add or delete any values

#Creating tuple
tp = (1,2,3,4,5,6,7,8,9,10)
print(tp)

#Editing number 2 with 11
#tp[1] = 11
#print(tp)
#TypeError: 'tuple' object does not support item assignment

#Creating tuple
tp1 = (1,)
print(tp1)

a = 1
b = 8
temp = a
a = b
b = temp

#or a,b = b,a

print(a,b)
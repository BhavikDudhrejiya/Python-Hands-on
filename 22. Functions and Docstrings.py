#Inbuilt function
a = 9
b = 8
c = sum((a,b))
print(c)

#Self Define function for printing "Welcom! You are in function"
def fun():
    return f'Welcom! You are in function'
print(fun())

#Self Define function for average
def average(a,b):
    '''This is an average function'''
    average = (a+b)/2
    return average
print(average.__doc__)
print(average(5,8))

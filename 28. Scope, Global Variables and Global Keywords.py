# l = 10 #Global variable
#
# def fun(num):
#     m = 8 #Local variables
#     print(l,m) #Here We have mention global variable and local variable
#     print(num,'I have printed')
#
# fun('This is me')
# print(l)

# l = 10 #Global variable
# def fun(num):
#     m = 8 #Local variables
#     global l #It change the glocal variable in define function
#     l = 45
#     print(l,m) #Here We have mention global variable and local variable
#     print(num,'I have printed')
#
# fun('This is me')
# print(l)

def Bhavik():
    x = 20
    def rohan():
        global  x
        x = 99
    print('Before calling rohan()', x)
    rohan()
    print('After calling rohan()', x)

Bhavik()
print(x)
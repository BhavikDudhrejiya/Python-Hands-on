#This function is helps to handle an errors
num1 = input('Enter number 1 : ')
num2 = input('Enter number 2 : ')
try:
    print('This is a sum of these two numbers is = ',
          int(num1)+int(num2))
except Exception as e:
    print(e)
print('This line is very important')
#Input function
print('Please enter your name : ')
name_input = input()

print('Bill Amount:', name_input)

print('Bill including 15% GST :', (int(name_input) + int(name_input) * 15/100))
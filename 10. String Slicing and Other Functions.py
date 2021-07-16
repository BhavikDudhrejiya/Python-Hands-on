mystr = "My name is Bhavik"

#String slicing
print(mystr[0:2])
print(mystr[3:7])
print(mystr[8:10])
print(mystr[11:])

#Slicing string with skipping two characters
print(mystr[0:5:2])
print(mystr[0::2])
print(mystr[::2])
#Checking length of the string
print(len(mystr))

#Slicing through negative numbers
"""M   y   _    n   a   m  e   _   i  s  _ B  h  a   v  i  k
   -17-16-15-14-13-12-11-10-9-8-7-6-5-4 -3-2-1"""
print(mystr[-17:-1])
print(mystr[-17:])

#Slicing string with skipping one character in negative index
print(mystr[0:5:-2])
print(mystr[0::-2])
print(mystr[::-2])

#Checking data type through boolean form result
name1 = "Bhavik Dudhrejiya"
name2 = "Bhavik"
name3 = "goku"

print(type(name1)) #Checking data type normal way

print('Checking name1 variable is alpha numeric or not : ',name1.isalnum())
print('Checking name2 variable is alpha numeric or not : ', name2.isalnum())

print('Checking name1 variable is alpha  or not : ', name1.isalpha())
print('Checking name2 variable is alpha  or not : ',name2.isalpha())

print('Checking name1 variable is digit  or not : ', name1.isdigit())
print('Checking name2 variable is digit  or not : ', name2.isdigit())

print('Checking name1 variable is space  or not : ', name1.isspace())
print('Checking name2 variable is space  or not : ', name2.isspace())

print('Checking name1 ends with ya : ', name1.endswith("ya"))
print('Checking name2 ends with ya : ', name2.endswith("k"))

print('Checking  How many a in name1 : ', name1.count('a'))
print('Checking  How many a in name2 : ', name2.count('B'))

print('Converting name3 into capitalized form :', name3.capitalize())
print('Converting name3 into upper form :', name3.upper())
print('Converting name3 into lower form :', name3.lower())
print('Finding index number of o in name3 : ', name3.find('o'))
print('Replacing Goku with Goku SSJ in name3 variable : ', name3.replace('goku', 'Goku SSJ'))

''' Please explore more string functions on google'''
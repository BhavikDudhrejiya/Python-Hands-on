#Creating empty dictionary
d1 = {}
print(type(d1))

#Creatig dictionary
d2 = {'Name':"Bhavik", "Surname":"Dudhrejiya", "Age":35}
print(d2)
print(d2['Name'])
print(d2['Surname'])
print(d2['Age'])

#Creating dictionary under dictionary
d3 = {'A':1, 'B':2, 'C':{'C1':1,'C2':2}}
print(d3)
print(d3['A'])
print(d3['B'])
print(d3['C'])

#Accessing value of dictionary of dictionary
print(d3['C']['C1'])
print(d3['C']['C2'])

#Adding or updating dictionary
d2['Education'] = 'Master of Commerce'
d2.update({'Height':5.8})
print(d2)

#Deleting from dictionary
del d2['Age']
print(d2)

#Creating copy of another dictionary
d4 = d2.copy()
print(d4)

#Extracting values through key
print(d2['Name'])
print(d2.get('Name'))

#Printing keys of dictionary
print(d2.keys())
print(d3.keys())

#printing items of the dictionary
print(d2.items())
print(d3.items())
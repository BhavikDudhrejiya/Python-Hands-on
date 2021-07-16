#Break
i = 0

while (True):
    print(i, end= ' ')
    if (i==44):
        break
    i+=1 # i = i+1

#Continue

while (True):
    if i+1>5:
        i = i+1
        continue #We are saying that continue printing an out when iteration fullfill given condition i.e. if value greater than 5
    print(i+1, end= ' ')
    if i==44:
        break #We are saying that stop printing an output until value reach 44
    i+=1 # i = i+1
# if i value greater than 5 print values until it reach 44



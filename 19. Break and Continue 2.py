while(True):
    inp = int(input("Enter a number:"))
    if inp>100:
        print('Congrats you have entered a number greater than 100\n')
        break
    else:
        print('Try again\n')
        continue
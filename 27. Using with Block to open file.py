# f = open('Bhavik.txt', 'r')
# #print(f.readlines())
# print(f.readline())


with open('Bhavik.txt') as f:
    a = f.read()
    print(a)
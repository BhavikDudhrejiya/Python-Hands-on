# # File IO Basics
# '''
# 'r' = Open file for reading - Default
# 'w' = Open a file for writing
# 'x' = Creates file if not exists
# 'a' = Add more content to a file
# 't' = Text mode
# 'b' = Binary mode
# '+' = 'Read and Write
# '''
#
# #Reading Bhavik.txt file
# f = open('Bhavik.txt', 'r')
# content = f.read()
# print(content)
#
# f = open('Bhavik.txt', 'rb')
# content = f.read()
# print(content)
#
# f = open('Bhavik.txt', 'rt')
# content = f.read()
# print(content)
#
# f = open('Bhavik.txt', 'rt')
# content = f.read(3)
# print(content)
#
# content = f.read(3)
# print(content)
# #Closing the file
#
#
# f = open('Bhavik.txt', 'rt')
# for i in f:
#     print(i, end = '')

f = open('Bhavik.txt', 'rt')
print(f.readline())
print(f.readline())
print(f.readline())

f = open('Bhavik.txt', 'rt')
print(f.readlines())

f.close()
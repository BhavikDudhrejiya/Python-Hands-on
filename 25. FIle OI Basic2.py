f = open('Bhavik.txt', 'w')
f.write('Bhavik is studying very hard')
f.close()

'''This function can replace the old content and rewrite over Bhavik.txt file'''

f = open('Bhavik.txt', 'a')
a = f.write('\nHe is a good boy')
print(a) #It shows count of text
f.close()

'''This function can add new content with existing content in Bhavik.txt file'''

f = open('Bhavik.txt', 'r+')
print(f.read())
f.write('Thank You\n')
print(f.read())
f.close()

'''This function can read the file and add new content with existing content in Bhavik.txt file'''
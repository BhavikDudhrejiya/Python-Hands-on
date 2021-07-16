#Creating empty set
s1 = set()
print(type(s1))

#Creating set
s2 = set([1,2,3,4,5,6,7,8,9,10])
print(s2)

#Creating set with some duplicate elements
s3 = set([0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0])
print(s3)

#Adding elements in a s1 set
s1.add(1)
print(s1)

#Adding multiple values in a s1 set
s1 = s1.union({2,3,4})
print(s1)

#s1 intersect with s2
s1 = s2.intersection()
print(s1)

#Checking two sets are disjoint or not i.e. is there any interaction or not
s5 = set([20,25,30,35,40])
s6 = set([50,55,60,65,70])
print(s6.isdisjoint(s5))
print(s2.isdisjoint(s1))

#Removing elements from set
print(s1)
s1.remove(1)
print(s1)

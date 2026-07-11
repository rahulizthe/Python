#Set methods.

#1 print length of the set.
s = {1,24,5,74,"rahul"}
print(len(s))

#2 add an element in a set.
s.add("abbas")
print(s)

#3 remove an element from a set.
s.remove(5)
print(s)

#4 clear all elements from a set.
s.clear()
print(s)#returns empty set.

#5 to pop an element from a set.
s1 = {1,"rahul",34.5,"","hi"}
s1.pop()#removes a random element from the set.
print(s1)

#6 Union of two sets.
s2={1,3,4,6}
s3={7,8}
set_union = s2.union(s3)#add all the values of s2 and s3.
print(set_union)

#7 Intersection of two sets.
s4={1,2,3,4,5,6,}
s5={1,2,3,4,5}
set_intersection = s4.intersection(s5)#removes all the values which are not common in s4 and s5.
print(set_intersection)
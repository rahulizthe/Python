# #solution 1
Fruits = []
# # #taking inputs for 7 fruits.
f1 = input("enter fruits name: ")
Fruits.append(f1)
f2 = input("enter fruits name: ")
Fruits.append(f2)
f3 = input("enter fruits name: ")
Fruits.append(f3)
f4 = input("enter fruits name: ")
Fruits.append(f4)
f5 = input("enter fruits name: ")
Fruits.append(f5)
f6 = input("enter fruits name: ")
Fruits.append(f6)
f7 = input("enter fruits name: ")
Fruits.append(f7)
print(Fruits)

# #solution 2
marks = []
# #input marks and sort them in ascending order.
m1 = int(input("enter marks : "))
marks.append(m1)
m2 = int(input("enter marks : "))
marks.append(m2)
m3 = int(input("enter marks : "))
marks.append(m3)
m4 = int(input("enter marks : "))
marks.append(m4)
m5 = int(input("enter marks : "))
marks.append(m5)
m6 = int(input("enter marks : "))
marks.append(m6)
m7 = int(input("enter marks : "))
marks.append(m7)
marks.sort()

# print(marks)

#solution 3
#proving tuple is immutable.
tuple1 = ("apple",23,5.6,"hello")
tuple1[2] =10 #not possible.

#solution 4
#program to sum all the item in a list.
l = [23,12,3,43,34,7]
#appraoch 1
sum1 = l[0]+l[1]+l[2]+l[3]+l[4]+l[5]
print(sum1)
#appraoch 2
print(sum(l))

#solution 5
#count the numbers of zeroes in tuple.
t =(0,3,4,5,0,10,0,2,0)
n = t.count(0)
print(n)


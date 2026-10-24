# list in python

# marks=[83,88,88,91,96]
# print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[4])
# print(len(marks))


   #it can store element of differents data types(int, float,str,etc)
#students=["vabhee",91,"A+","vivek",90,"A-"]
# print(len(students))
# print(students)

# stringe is inmutable and List  is mutable(elements of list can change)
#students[0]="vabhiii"
#print(students)

#list slicing     (similer string slicing)
# marks=[83,85,91,90,96,100]
# print(marks[1:4])           #ending idx is not included
# print(marks[:5])
# print(marks[2:])
# print(marks[-3:-2])

#list methods
 
# list=[2,1,4]
# list.append(7)   #add 7 at the end of list
# list.sort()   # sort in ascending order
# print(list)
# list.sort(reverse=True)   #sort in descending order
#list.reverse()            #reverse list
# list.insert(3,7)     #insert element at that indx
# list.insert(1,5)     

# print(list)

# list=[2,1,5,1,3,1]
# list.remove(1)  #removes first occurence of elements
# list.pop(3)      #removes elements at indx
# print(list)


#tuples in python       immutable sequences of values

# tup=(2,1,5,9,6)
# print(type(tup))
# print(tup[1])
# print(tup[0])

# tup=()
# print(tup)
# print(len(tup))

# tup=(2,)
# print(tup)
# print(type(tup))

#slicing in tupels is same as list & string


#tu

#tuple Methods

# tup=(2,4,1,5,1,6)
# print(tup.index(4))
#ind=tup.index(1)    #return indx of first occurrence
#moye=tup.count(1)    #return total occurence of element
#print(moye)

#WAP to ask the user to enter names of their 3 favorite movies &store them in a list
# movies=[]
# m1=input("enter m1")
# m2=input("enter m2:")
# m3=input("enter m3:")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)

# movies=[]
# movies.append(input("enter m1"))
# movies.append(input("enter m2"))
# movies.append(input("enter m3"))
# print(movies)

#WAP to check if a list contains a palindrome of elements. (hint ; use copy() method)
# palindrome means any list and their reverse list are same
# l1=[1,2,3,2,1]
# l2=l1.copy()
# l2.reverse()
# if(l1==l2):
#     print("yes")
# else:
#     print("no")
# print(l2)

#WAP to count the number of students with the "A" grade in the following tuple.
# grade=("C","D","A","A","B","B","A")
# count=grade.count("A")
# print(count)
#store those values in alist &sort them from "A" to "D".
# glist=["C","D","A","A","B","B","A"]
# glist.sort()
# print(glist)


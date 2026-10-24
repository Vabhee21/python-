#LOOPS (used to repeat instruction)

  #While Loops
# count=1
# while count<=5:
#     print("hello")
#     count+=1
# print(count)

#print number 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i+=1

#print number from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

#print 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

#print multiplication table of anumber n.
# n=int(input("enter number:"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

#print the elements of the following list using a loop.
#[1,4,9,25,36,49,64,81,100]
# l1=[]
# i=1
# while i<=10:
#     l1.append(i*i)
#     i+=1
# print(l1)

  #or
# l1=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<10:
#     print(l1[idx])
#     idx+=1

#search for a number x in this tuple using loop
# t1=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("x:"))
# i=0
# while i<len(t1):
#     if(t1[i]==x):
#         print("index of x is ",i)
#     i+=1

#break & continue
# i=0
# while i<=6:
#     print(i)
#     if(i==3):
#         break
    
#     i+=1

# i=0
# while i<=6:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

#print even numbers
# i=1
# while i<=20:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1


## FOR loops     ()

   #List
# num=[1,2,3,4,5]
# for val in num:
#     print(val)

   #tuples
# veggies=["potato","brinjal","ladyfinger","cucumber"]
# for val in veggies:
#     print(val)

# tup=(1,2,3,4,5,6,7,8)
# for val in tup:
#     print(val)

    #string
# str="my name is vabhee" 
# for ch in str:
#     print(ch)

# strr="mymindset"
# for ch in strr:
#     if(ch=="n"):
#         print("found")
#         break
#     continue
        
    

        
#print the element of the following list using a loop
# l1=[1,4,9,16,25,36,49,64,81,100]
# for el in l1:
#     print(el)

#search for a number x in this tuple usin loop
# x=int(input("x:"))
# t1=(1,4,9,16,25,36,49,64,81,100)
# for el in t1:
#     if(el==x):
#         print("found")
#         break
#     continue
# else:
#     print("not found")

# i=0
# for el in t1:
#     if(el==x):
#         print("found at index",i)
#         break
#     i+=1
# else:
#     print("not found")

#range()

# seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

# for i in range(10):  #range(stop)
#     print(i)

# for i in range(2,10):  #range(start,stop)
#     print(i)
 
# for i in range(2,10,2):  #range(start,stop,end)
#     print(i)

# for i in range (2,11,2):  # even numbers
#     print(i)

#print number from 1 to 100.
# for i in range(1,101):
#     print(i)

#print number number from 100 to 1
# for i in range(100,0,-1):
#     print(i)

#print multiplication table of number n
# n=int(input("n:"))
# for i in range(1,11):
#     print(i*n)

#pass statement
# for i in range(5):    # loop wala part execute nahi hoga 
#     pass
# print("some useful work")

#WAP to find the sum of first n numbers .(using while)
# n=int(input("n:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i=i+1
# print(sum)

#using for loop
# n=int(input("n:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#WAP to find the factorial of  n .(using for ) 
# n=int(input("n:")) 
# fact=1   
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

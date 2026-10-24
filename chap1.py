# print("hello world")
# print("my name is vabhee maurya .", "my age is 20." )
# print(40)
# print(60+40)
# name = "vabhee"  #string
# age = 23          #int
# price = 35.78     #float
# age2=age
# print(age)
# old=True
# a=None
# print(age)
# print(name)
# print(price)
# print("my name is :",name)
# print("my age is :",age)
# print("my price is :",price)
#print(age2)
# print(type(name))
# print(type(age))
# print(type(price))
# print(type(old))
# print(type(a))

# a=6
# b=8
# sum=a+b
# print(sum)
# print(60-50)

# python is implicit because here type of variable is not declared 

#operator precedence pdh le
#expression execution
#1. string and numeric values operate together with *
# a,b=2,4
# txt="@"
# print(2*txt*4)
# print(3*"$"*1)

# 2. string & string can operat with +
# A="4"
# print((A+txt)*3)

#3.numeric value can operate with all arithemetic operators
# print(5+4*8/2)
4. #result of division operator with two integers wiil be float
#5. integer division with float and int will give int displayed as float 

# print(5//2)
# print(5.0//2)
# floor gives closest integer, which is lesser than or equal to the float value
#result of (A//B) gives as floor(A/B)
#reminder is negative when demoninator is negative but reminder is positive when nemonitor is negative
# print(5%-2)
# print(-5%2)


  #coments in python
#single line comments
"""this is
 multiline
   line
     comments"""


#input in python  -  input()
#string input
# name=input("name :")
# print(name)

#int input
# age=int(input("age:"))
# print(age)

#float input
# price=float(input("float :"))
# print(price)

#print("my name is ",name, "my age is ",age,"my price is ",price)



#conditional statements (if-elif-else)
#use indentation (proper spacing)  4space 

#traffic light code
# light=input("enter light color:")
# if(light=="yellow"):
#     print("ready for ")
# elif(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# else:
#     print("traffic light is broken")

#Grades of students
# marks=int(input('Enter marks:'))
# if(marks>=90):
#     print("grade A")
# elif(marks<90 and marks>=70):
#     print("grade B")
# elif(marks<70 and marks>=60):
#     print("grade C")
# elif(marks<60 and marks>=45):
#     print("grade D")
# else:
#     print("you can do it in next time")

#single line if 0r Ternary operator
# food=input("food:")
# eat="yes" if food=="cake" else "no"
# print(eat)

# food=input("food:")
# print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")

#clever if or ternary operator
# age=int(input("enter your age :"))
# vote=("yes","no") [age<18]
# print(vote)
# sal=int(input("enter you salary:"))
# tax=sal*(0.1,0.2) [sal>=50000]
# print(tax)


#types of operators
   #arthemetic(+,-,*,/,%,**,//)
# print(29%4)  #reminder
# print(2**3)   #2^3

    #relational operrators(==,!=,>,<,>=,<=) give output in boolean(True or False)
    #assingnment operators(=,+=,-=,/=,%=,**=)

    #logical operators(not,and,or)


#type conversion    
# a=2
# b=4.25
# sum =a+b
# print(sum)

#type casting 
# a,b=2.25,"4"
# b=int("4")
# sum=a+b
# print(sum)
# a=4
# b=int(6.25)
# print(b)
# sum = a+b
# print(sum)
# print(type(b))

# val=input("enter some value :")
# print(type(val),val)

# num1=int(input("enter num1:"))
# num2=int(input("enter num2 :"))
# sum=num1+num2
# print(sum)

#WAP to input side of a square & print its area.
# side=float(input("enter side of square:"))
# are=side*side
# print(are)

#wap to input 2floating numbers &print their average 
# a=float(input("enter num1:"))
# b=float(input("enter num2:"))
# avg=(a+b)/2
# print(avg)

#wap to input 2 int numbers a,b.print True if a is greater than or equal to b.if not print false 
# a=int(input("num1=:"))
# b=int(input("num2=:"))
# print(a>=b)





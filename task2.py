#Answer1
# x=int(input("enter a number"))
# if x%3==0 and x%5==0:
#     print("Consultadd Python Training")
# elif x%3==0:
#     print("Consultadd")
# elif x%5==0:
#     print("c")
# else: print("not divisible by 3 or 5")

#Answer2
# a=int(input("enter a number between 1-5:"))
# if a==1:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter first number:"))
#     result=num1+num2
#     if result < 0:
#         print("NEGATIVE")
#     else: print("Addition of the two numbers gives result as:",result)
# elif a==2:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter first number:"))
#     result=num1-num2
#     if result < 0:
#         print("NEGATIVE")
#     else: print("Subtraction of the two numbers gives result as:",result)
# elif a==3:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter first number:"))
#     result=num1/num2
#     if result < 0:
#         print("NEGATIVE")
#     else: print("Division of the two numbers gives result as:",result)
# elif a==4:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter first number:"))
#     result=num1*num2
#     if result < 0:
#         print("NEGATIVE")
#     else: print("Multiplication of the two numbers gives result as:",result)
# elif a==5:
#     num1=int(input("enter first number:"))
#     num2=int(input("enter first number:"))
#     result=(num1+num2)/2
#     if result < 0:
#         print("NEGATIVE")
#     else: print("Average of the two numbers is:",result)
# else:
#         print("Invalid input")

#Answer3
# a=10
# b=20
# c=30
# avg = (a+b+c)/3
# print("avg=",avg)
# if avg>a and avg>b and avg>c:
#     print("avg is higher than a,b,c")
# elif avg>a and avg>b: 
#     print("avg is higher than a,b")
# elif avg>a and avg>c:
#     print("avg is higher than a,c")
# elif avg>b and avg>c:
#     print("avg is higher than b,c")
# elif avg>a:
#     print("avg is just higher than a")
# elif avg>b:
#     print("avg is just higher than b")
# elif avg>c:
#     print("avg is just higher than c")

#Answer4
# while True:
#     num=int(input("Enter a number:"))
#     if num<0:
#         print("It's Over")
#         break
#     elif num>0:
#         print("Good Going")
#     else:
#         pass

#Answer5
# for x in range(2000,3201):
#     if x%5!=0 and x%7==0:
#         print(x)

#Answer6
#1)it will not execute as x is int type and not string
#2)it will print 0 error 1 error 2
#3)it will print 0 1 2 3 4 

#Answer7
# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

#Answer8
# txt=input("Enter a string :")
# digit=letter=0    
# for j in txt:
#     if j.isdigit():
#         digit+=1
#     elif j.isalpha():
#         letter+=1
#     else:
#         pass
# print("Letters:",letter)
# print("Digits:",digit)

#Answer9 Part1
# while True:
#     guess=int(input("Guess the lucky number:"))
#     if guess==24:
#         break

#Answer9 Part2
# while True:
#     number=int(input("Guess the lucky number:"))
#     if number==24:
#         break
#     else:
#         answer=input("Do you want to keep guessing?")
#         if answer=="no":
#             break
#         else:
#             pass

#Answer10 & 11
# counter=1
# while counter<=5:
#     print("Type in the",counter,"number")
#     answer=int(input("Enter the number:"))
#     if answer==24:
#         print("Good Guess!")
#         break
#     else:
#         print("Try Again!")
#         counter=counter+1
#         if counter==6:
#             print("Game Over!")
#             print("Sorry but that was not very successful")
#         else:
#             pass








 
    
   
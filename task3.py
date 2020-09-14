#Answer1
# list=[1,2,3,4,2.3,4.5,6.7,7.8,'a','word']
# print(list)

#Answer2
# list1=[1,2,3,4,5]
# print(list1[:3])

#Answer3
# list2=[1,2,3,4]
# print("Sum of the elements in the list:",sum(list2))
# sum=0
# product=1
# for i in list2:
#     sum+=i
#     product*=i
# print("Sum:",sum)
# print("Product:",product)

#Answer4
# x=[1,2,3,4,5,6,7]
# print("maximum value:",max(x))
# print("minimum value:",min(x))

#Answer5
# list3=[1,2,3,4,5,6,7,8,9,10]
# list4=[]
# for i in list3:
#     if i%2==0:
#         continue
#     else:
#         list4.append(i)
# print(list4)

#Answer6
# list5=[]
# for i in range(1,31):
#     if i<=5 or i>=26:
#         square=i*i
#         list5.append(square)
#     else:
#         continue
# print(list5)

#Answer7
# list1=[1,3,5,7,9,10]
# list2=[2,4,6,8]
# for i in list1:
#     if i==list1[-1]:
#         list1.remove(i)
# list1.extend(list2)
# print(list1)

#Answer8
# a={1:10,2:20}
# b={3:30,4:40}
# a.update(b)
# print(a)

#Answer9
# dict={}
# for i in range(1,6):
#     dict[i]=i*i
# print(dict)

#Answer10
# x=input("Enter comma separated numbers:")
# y=x.split(',')
# list1 =[]
# for i in y:
#     list1.append(i)
# print(list1)
# tuple1=tuple(list1)
# print(tuple1)

#question 11 & 12 are repeated questions

#Answer13
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# a=x[5]
# print(a[0:4])
# print(x[-3:-1])
# print(x[::2])
# print(x[::-1])
# print(x[5][5][0])

#Answer14
#range and xrange exists in python2.x whereas in python3.x xrange was renamed as range
# for i in range(1,1001):
#     print(i)
# for i in xrange(1,1001):
#     print(i)

#Answer15
#1)tuples are faster than lists since it remains fixed it can be used for iterations.
#2)it keeps your code safe since the data is write protected as tuples are immutable.
#3)some tuples can be used as dictionary keys but lists cannot be used for same purpose as it is mutable.

#Answer16
# list1=[]
# for i in range(1,100):
#     if i%3==0 and i%2==0:
#         list1.append(i)
# print(list1)

#Answer17
# string="consultadd"
# string1=string[::-1]
# print(string1)
# count=0
# for i in string1:
#     count+=1
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         print(i,count-1,sep=',',end=' ')

#Answer18
# string="hello my name is abcde"
# list=string.split(" ")
# for i in list:
#     if len(i)%2==0:
#         print(i)

#Answer19
# x=[1,2,3,4,5,6,7,8,9,-1]
# for i in x:
#     for j in x:
#         if i+j==8 and i!=j:
#             print(i,j)

#Answer20
# even_list=[]
# odd_list=[]
# even=len(even_list)
# odd=len(odd_list)
# while even<5 and odd<5:
#     even=len(even_list)
#     odd=len(odd_list)
#     number=int(input("Enter a number between 1-50:"))
#     if number%2==0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)
# print(even_list)
# print(odd_list)
# print("Sum of even_list:",sum(even_list))
# print("Sum of odd_list:",sum(odd_list))
# print("Maximum value in even_list:",max(even_list))
# print("Maximum value in odd_list:",max(odd_list))

#Answer21
# x='12abcbacbaba344ab'
# list1=[]
# for i in x:
#     list1.append(i)
# list1.sort()
# k=''
# for j in list1:
#     if j.isalpha():
#         if k==j:
#             continue
#         else:
#             k=j
#             list1.count(k)
#             print(k,list1.count(k))
#     else:
#         continue

#Answer22
# x=(1,2,3,4,5,6,7,8,9,10)
# y=[]
# for i in x:
#     if i%2==0:
#        y.append(i)
#     else:
#         pass
# z=tuple(y)
# print(z)



            


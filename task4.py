#Answer1 using slicing concept
# def reverse_string(txt):
#     print("reverse string:",txt[::-1])
# reverse_string('1234abcd')

#Answer1 using for loop
# def reverse_string(txt):
#     i=len(txt)-1
#     txt1=''
#     for x in range(i,-1,-1):
#         txt1=txt1+txt[x]
#     print(txt1)
# reverse_string('1234abcd')

#Answer2
# def count_case(txt):
#     up=0
#     low=0
#     for i in txt:
#         if i.isupper():
#             up+=1
#         elif i.islower():
#             low+=1
#     print("No. of Upper case characters:",up)
#     print("No. of Lower case characters:",low)
# count_case("AbcBCDeEFf123")

#Answer3
# def remove_duplicate(list1):
#     list2=[]
#     for i in list1:
#         if i in list2:
#             continue
#         else:
#             list2.append(i)
#     print(list2) 
# remove_duplicate([1,2,2,3,3,3,4,5,5,6,7])

#Answer4
# def sort_string(txt):
#     x=txt.split("-")
#     x.sort()
#     y=''
#     for i in x:
#         if i==x[0]:
#             y=y+i
#         else:
#             y=y+'-'+i
#     print(y)
# sort_string("apple-orange-banana-mango")

#Answer5
# def upper_case(txt):
#     print(txt.upper())
# upper_case("Hello world")
# upper_case("Practice makes man perfect")

#Answer6
# def add_int(txt1,txt2):
#     x=int(txt1)
#     y=int(txt2)
#     print("Sum of the integers:",x+y)
# add_int('11','42')

#Answer7
# def max_length(txt1,txt2):
#     if len(txt1) > len(txt2):
#         print(txt1)
#     elif len(txt1)==len(txt2):
#         print(txt1)
#         print(txt2)
#     else:
#         print(txt2)
# max_length("practice","perfect")
# max_length("promises","pressure")
# max_length("practice","perfection")

#Answer8
# def square_tuple():
#     x=[]
#     for i in range(1,21):
#         x.append(i**2)
#     print(tuple(x))
# square_tuple()

#Answer9
# def label_number(limit):
#     for i in range(0,limit+1):
#         if i%2==0:
#             print(i,"EVEN")
#         else:
#             print(i,"ODD")
# label_number(3)

#Answer10
# y=filter(lambda x:x%2==0,range(1,21))
# print(list(y))

#Answer11
# y=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])
# z=map(lambda x:x**2,list(y))
# print(list(z))

#Answer12
# def divide_byzero():
#     try:
#         x=5/0
#         print(x)
#     except:
#         print("division by zero is not defined")
# divide_byzero()

#Answer13
# from functools import reduce
# a=reduce(lambda x,y:x+y,[[1,2,3],[4,5],[6,7,8]])
# b=reduce(lambda x,y:str(x)+str(y),[1,2,3,4,5,6,7])
# print(a)
# print(b)

#Answer14(i)
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
# output=2 since finally block is executed independent of any case

#Answer14(ii)
# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()
# output=after f and NameError: name 'f' is not defined 
# since try block is not having a corresponding catch block 
# thats why error is detected but not handled
# def login():
#     print("python")
# login()

# def add():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# add()

# def login(username,password):
#     print(f"your username is:{username},and your password is:{password}")
# login("sunil","battle")

# def multiply(a,b):
#     print(a*b)
# multiply(2,3)

# def pw(x,y):
#     z=x**y
#     print(z)
# pw(5,2)

# def show(name,age):
#     print(f"name:{name} age:{age}")
# show(name="sunil",age=20)

# def show(name,age=20):
#     print(name,age)
# show(name="sunil")

# def show(**num):
#     z=num['a']+num['b']+num['c']
#     print(z)
# show(a=5,b=4,c=3)

# def add(a,b):
#     c=a+b
#     d=a-b
#     return c,d
# m=add(24,7)
# print(m)




# def sum(a,b):
#     c=a+b
#     print(c)
# sum(2,3)

# def greatest():
#     a=int(input("enter 1st number"))
#     b=int(input("enter 2nd number"))
#     c=int(input("enter 3rd number"))
#     if a>b and a>c:
#         return a
#     elif b>a and b > c:
#         return b
#     else:
#         return c


# def add():
#     a=10
#     b=20
#     print(a+b)
# add()

# def paree(a,b):
#     sum=a+b
#     return sum
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# c=paree(x,y)
# print(c)

# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()
# disp()

# def disp():
#     def show():
#         return "show function"
#     result=show()+"disp function"
#     return result
# a=disp()
# print(a)

# def inner():
#     x=4
#     print(x)
# inner()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         print(x)
#         print("inside the function y", y)
#     inner()
#     print("z:",z)
# outer()

# x=10
# def outer():
#     x=4
#     def inner():
#         x=8
#         print(x)
#         print("inside the function y",)
#     inner()
#     print("z:",)
# outer()

# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner:",x)
#     print(x)
#     inner()
#     print("outer:",x)
# outer()

# li=[5,7,22,97,54,62,77,23,73,61]
# square_list=list(map(lambda x:x**2,li))

# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x:x%2==0,data))

# print(var)

from functools import reduce


li=[5,8,10,20,50,100]
sum= reduce((lambda x,y:x+y),li)
print(sum)

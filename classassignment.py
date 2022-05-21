# a=input("enter a word")
# b=""
# for i in reversed(a):
#     b+=i
# print(b)


# from re import A


# a=1
# sum=0
# while a<=10:
#      sum=sum+a
#      a=a+1
# print(sum)

# for i in range (0,9):
#     if i%2==0:
#         print(i)

# a=[1,2,3,4,5,6,7,8,9]
# for i in range(len(a)):
#     if(i%2==0):
#         print(a[i])

# a=2
# b=3
# print(a,b)
# a,b=b,a
# print(a,b)

# a="programming"
# for i in range(len(a)):
#     if(i%2==0):
#         print(a[i],end="")

# a="programming"
# for i in range(len(a)):
#     if(i%2!=0):
#         print(a[i],end="")

# a="parameter"
# print(len(a))


# a=[8,2,3,-1,7]
# mult=1
# for i in a:
#     mult=mult*i
# print(mult)

# a=[8,2,3,0,7]
# sum=1
# for i in a:
#     sum=sum+i
# print(sum)

x=int(input("enter a number"))
if x%3==0 and x%5==0:
    print("FizzBuzz")
elif x%5==0:
    print("Buzz")
elif x%3==0:
    print("Fizz")
else:
    print(x)


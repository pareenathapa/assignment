# count = 0
# balance = 100000
# while count < 5:
#     cred = input("enter your name")
#     count += 1
#     if cred == "Pareena":
#         print("your credentials match")
#         c = int(input("Enter amount of money you want to withdraw"))
#         count = 100
#         if c <= balance:
#             pass  # withdraw money
#             print("you money was withdrawn")
#             break
#         else:
#             print("your withdraw balance excedded your limit")
#     else:
#         print("your credential do not match")
#     if count == 100:
#         exit()
#     if count == 3:
#         pass  # block the account
#         print("your account has been terminated.Please contact the Main office for renew")
#         exit()


# username=input("enter username:")
# password=input("enter password:")

# for i in range(0,3):
#     print("enter your credentials")
#     username1=input("enter your username:")
#     password1=input("enter your password:")
#     if username==username1 and password==password1:
#         print("you are successfully logged.")
#         break
#     else:
#         if(username!=username1 or password!=password1):
#             print("invalid credentials")
#         else:
#             print("3 attempt finished")


# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print("")


# 1. Write a program to accept percentage and display the Category according to the  following criteria :

# Percentage	Category
# < 40	                     Failed
# >=40 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent
# """

# perc=10000
# while perc>100:
#     perc=float(input("enter percentage you have obtained"))
# if perc<40:
#     print("failed")
# elif(perc<55):
#     print("fair")
# elif(perc<65):
#     print("good")
# else:
#     print("excellent")


# """


# 2. Write a Python Program to Swap Two Variables.

# """
# a=100
# b=200
# a,b=b,a 
# print(a,b)


# """


# 3. Write a program to print multiplication table of a  number 10 using for loop.
# """

# mult=int(input("enter the number you want multiplication table of"))
# for i in range(1,11):
#     print(f"{mult} + {i} = {mult*i}")


# """

# 4. Print list in reverse order using a loop. Hint: list1=[1,2,3,4]
# """
# a=[1,2,3,4]
# b=[]
# for i in reversed(a):
#     b.append(i)
# print(b)

# """

# 5. Display numbers from -10 to -1 using for loop.
# """
# for i in range(-10,0,1):
#     print(i)

# """

# 6. Use else block to display a message “Done” after successful execution of for loop
# """
# for i in range(10):
#     print(i)
# else:
#     print("done")

# """

# 7. Find the factorial of a number 5.
# """
# value=1
# fact = int (input("enter a number you want a factorial of :"))
# for i in range{fact,0,-1}:
#     value=value*i 5!=5*4*3*2*1=120
# print{f"the factorial of number is {value}"}

# """


# 8. Use a loop to display elements from a given list present at odd index positions. Given: 
# my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]
# """
# my_list=[10,20,30,40,50,0,70,80,90,100]
# for i in range(-1,len(my_list)):
#     if i%2!=0:
#         print(my_list[i])

# """

# 9. Calculate the cube of all numbers from 1 to a given number. (1-6)
# example:
# Expected output:
# 1-1
# 2-8
# 3-27
# 4-64
# 5-125
# 6-216
# """
# a= int (input("enter the number you want the cube of:"))
# for i in range(0,a+1):
#     print{f"{i}-{i**3}"}

# """


# 10.  Print First 10 natural numbers using for loop.
# """
# a=int(input("enter your number up to which you want to print: "))
# for i in range(1,a+1):
#     print(i)

# """

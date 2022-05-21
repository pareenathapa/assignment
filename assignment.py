# 1.  Write a Python function to multiply all the numbers in a list.
# Sample list = [8,2,3,-1,7]

# def multiply():
#     a=1
#     list=[8,2,3,-1,7]
#     for i in list:
#         a=a*i
#     return a
# print(f"your multiplication value is{multiply()}")

# 2.  Write a Python function to sum all the numbers in a list.
# Sample list : [8, 2, 3, 0, 7]

# def sum():
#     a=0
#     list=[8,2,3,0,7]
#     for i in list:
#         a=a+i
#     return a
# print(f"total sum is{sum()}")


# 3.  Write a python function to find min of three numbers.(no parameter and no return type)

# def smallest(): 
#     a=int(input("enter the first letter"))
#     b=int(input("enter the second letter"))
#     c=int(input("enter the third letter"))
#     if a<b and a<c:
#         print(f"{a} is the smallest among three numbers")
#     elif b<a and b<c:
#         print(f"{b} is the smallest among three numbers")
#     else:
#         print(f"{c} is the smallest among three numbers")
# smallest()


# 4. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fizz_buzz():
    a=int(input("enter a number"))
    if a%3==0:
        return("Fizzbuzz")
    elif a%3==0:
        return ("fizz")
    elif a%5==0:
        return ("buzz")
    else:
        return a
print(fizz_buzz())

# i=1
# while(i<=5):
#     print("pareena")
#     i=i+1

# i=1
# while(i<=10):
#     print(i)
#     i=i+3


# i=1
# while(i<=10):
#     print('2*',i,'=',2*1)
#     i=i+1

# a=[1,2,3,4]
# sum=0
# i=0
# list=len(a)
# while(i<list):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# original_list=[1,2,3,4]
# b=[]
# i=len(original_list)-1
# while i>=0:
#     b.append(original_list[i])
#     i=i-1
# print(b)


# count = True
# while count:
#     c = input("enter a alphabet")
#     if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
#         pass
#     else:
#         count += 1
#     if count == 3:
#         exit()


a=input("enter any vowel letter")
while a!='a' and a!='e' and a!='i' and a!='o' and a!='u':
    a=input("enter right vowel letter")
print("you typed:",a)

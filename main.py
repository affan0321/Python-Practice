# n=int(input("Enter a number"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)    

# n= int(input("Enter a number"))
# sum = 0
# for i in range(1,n+1):
#     if i% 2 == 0:
#         sum = sum + i
# print(sum)        


# n = (int(input("Enter a number to check its factors")))
# for i in range (1 , n+1):
#     if n%i == 0:
#         print(i)

# n = int(input("Enter a number to check if its a perfect number"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("Its a perfect number")
# else:
#     print("Its not a perfect number")    

n = int(input("Enter a number to check if its a prime number or not"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1

if count <=2:
    print("Its a prime number")
else:
    print("It is not a prime number")    
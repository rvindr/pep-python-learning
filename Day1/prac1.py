
# print table
# num = int(input("Enter number: "))

# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")


# palindrome
# num = int(input("Enter number: "))
# original = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print("Number is palindrome" if rev == original else "Number is not palindrome")


# def checkPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# print(checkPrime(10))


# n = 4
# num = 1

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()


# n = 4

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# ****
# *  *
# *  *
# ****

n = 5

for i in range(1, n):
    print(2 * i)

for j in range(n, 0, -1):
    print(2 * j, end=" " if j != 1 else "")
print()

for i in range(n - 1, 0, -1):
    print(2 * i)






# Factorial
# def factorial(n):
#     assert n >= 0 or int(n) == n, "The number must be positive integer only!"
#     if n == 1:
#         return n
#     return n * factorial(n-1)

# n = int(input("Please inter number: "))
# print(factorial(n))

# Fibonacci numbers

# def fibonacci(n):
#     assert n >= 0 or int(n) == n, "The number must be positive integer only!"
#     if n == 1 or n == 0:
#         return n 
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Please inter number: "))
# print(fibonacci(n))


# def sumOfDigits(num):
#     if len(str(num)) == 1:
#         return num
#     if len(str(num)) >= 2:
#         return int(num % 10) + sumOfDigits(int(num // 10))

# num = int(input("inter number"))
# print(sumOfDigits(num))
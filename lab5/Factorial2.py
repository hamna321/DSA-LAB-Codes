'''Factorial using loop'''
def factorial_with_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
num = 5
print(f"Factorial of {num} is {factorial_with_loop(num)}")

def calculate_exponential(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
s
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = calculate_exponential(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")


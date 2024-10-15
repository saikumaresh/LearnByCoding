def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(2))
print(factorial(5))
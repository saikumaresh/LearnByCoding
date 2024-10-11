def fibonacci(n):
    if(n == 0): # Base Condition 1
       return 0
    if (n == 1): # Base Condition 2
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # Main Logic

number = 10
for i in range(1, number):
    print(fibonacci(i), end = " ")
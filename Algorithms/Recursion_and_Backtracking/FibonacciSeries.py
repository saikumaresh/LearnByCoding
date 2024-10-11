def fibonacci(n):
    if(n == 0):
       return 0
    if (n == 1): 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

number = 10
for i in range(1, number):
    print(fibonacci(i), end = " ")
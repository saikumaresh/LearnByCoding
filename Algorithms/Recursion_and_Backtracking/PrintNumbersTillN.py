def print_num(n):
    if n == 1: # Base Condition
        print(1)
        return
    print_num(n-1) # Main Logic
    print(n)
    return
print_num(10)
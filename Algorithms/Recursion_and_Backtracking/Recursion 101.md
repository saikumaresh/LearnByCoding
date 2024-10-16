# 1. What will be the output of following program ?

```python

def bar(x, y):
    # If y is 0, return 0
    if y == 0:
        return 0
    # Otherwise, recursively call bar and add x
    return (x + bar(x, y - 1))

def foo(x, y):
    # If y is 0, return 1
    if y == 0:
        return 1
    # Otherwise, call bar with x and the result of foo(x, y - 1)
    return bar(x, foo(x, y - 1))

# Example usage
print(foo(3, 5))  # Output: 243

```
## Iteration Breakdown for print(foo(3, 5))
foo(3, 5):

Calls bar(3, foo(3, 4)).
foo(3, 4):

Calls bar(3, foo(3, 3)).
foo(3, 3):

Calls bar(3, foo(3, 2)).
foo(3, 2):

Calls bar(3, foo(3, 1)).
foo(3, 1):

Calls bar(3, foo(3, 0)).
foo(3, 0):

Returns 1.

Now substituting back up the call stack:

Return to foo(3, 1):

Calls bar(3, 1):
bar(3, 1) returns 3 + bar(3, 0) → 3 + 0 = 3.
Thus, foo(3, 1) returns 3.
Return to foo(3, 2):

Calls bar(3, 3):
bar(3, 3) returns 3 + bar(3, 2).
bar(3, 2) returns 3 + bar(3, 1) → 3 + 3 = 6.
So, bar(3, 3) returns 3 + 6 = 9.
Thus, foo(3, 2) returns 9.
Return to foo(3, 3):

Calls bar(3, 9):
bar(3, 9) returns 3 * 9 = 27.
Thus, foo(3, 3) returns 27.
Return to foo(3, 4):

Calls bar(3, 27):
bar(3, 27) returns 3 * 27 = 81.
Thus, foo(3, 4) returns 81.
Return to foo(3, 5):

Calls bar(3, 81):
bar(3, 81) returns 3 * 81 = 243.

## Final Result
The final result of print(foo(3, 5)) is 243.


# 2. What will be the output of following program ?

```python

def fun(x, n):
    # Base case: If n is 0, return 1 (as any number to the power of 0 is 1)
    if n == 0:
        return 1
    # If n is even, recursively call fun with x squared and n halved
    elif n % 2 == 0:
        return fun(x * x, n // 2)
    # If n is odd, multiply x with the result of fun with x squared and (n-1) halved
    else:
        return x * fun(x * x, (n - 1) // 2)

# Call the function with x = 2 and n = 10
ans = fun(2, 10)
# Print the result
print(ans)  # Output: 1024

```

## Iterations
Let’s break down the iterations when fun(2, 10) is called:

Call 1: fun(2, 10)

𝑛
n is even.
Calls fun(4, 5)
Call 2: fun(4, 5)

𝑛
n is odd.
Calls 4 * fun(16, 2)
Call 3: fun(16, 2)

𝑛
n is even.
Calls fun(256, 1)
Call 4: fun(256, 1)

𝑛
n is odd.
Calls 256 * fun(65536, 0)
Call 5: fun(65536, 0)

𝑛
n is 0.
Returns 1.
Now, we can backtrack through the calls:

Call 4 returns 256 * 1 = 256.
Call 3 returns 256.
Call 2 returns 4 * 256 = 1024.
Call 1 returns 1024.

## Output
Finally, when we execute print(ans), the output will be:
1024
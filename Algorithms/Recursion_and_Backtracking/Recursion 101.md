What will be the output of following program ?

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
Iteration Breakdown for print(foo(3, 5))
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

Final Result
The final result of print(foo(3, 5)) is 243.
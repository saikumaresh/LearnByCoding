def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(2))
print(factorial(5))

#########################################

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==1:
            return 1
        return self.solve(A-1)*A
    
sol = Solution()
print(sol.solve(2))
print(sol.solve(5))
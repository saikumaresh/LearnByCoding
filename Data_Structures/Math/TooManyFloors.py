# ### Problem Statement: Too Many Floors
# Chef and Chefina are residing in a hotel. There are 10 floors in the hotel, and each floor consists of 10 rooms.

# - Floor 1 consists of room numbers 1 to 10.
# - Floor 2 consists of room numbers 11 to 20.
# - ...
# - Floor i consists of room numbers `10 * (i - 1) + 1` to `10 * i`.

# You know that Chef's room number is `X` while Chefina's room number is `Y`. If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

# ### Input Format
# - The first line will contain `T`, the number of test cases.
# - Each test case consists of a single line of input, two integers `X`, `Y`, the room numbers of Chef and Chefina respectively.

# ### Output Format
# - For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

# ### Constraints
# - 1 ≤ T ≤ 1000
# - 1 ≤ X, Y ≤ 100
# - X ≠ Y

# ### Sample Input
# ```
# 4
# 1 100
# 42 50
# 53 30
# 81 80
# ```

# ### Sample Output
# ```
# 9
# 0
# 3
# 1
# ```

# ### Explanation:
# - Test Case 1: 
#   - Room `1` is on the 1st floor, and room `100` is on the 10th floor. Chef needs to climb 9 floors to reach Chefina's room.

# - Test Case 2: 
#   - Room `42` is on the 5th floor, and room `50` is also on the 5th floor. Chef does not need to climb any floor.

# - Test Case 3: 
#   - Room `53` is on the 6th floor, and room `30` is on the 3rd floor. Chef needs to go down 3 floors to reach Chefina's room.

# - Test Case 4: 
#   - Room `81` is on the 9th floor, and room `80` is on the 8th floor. Chef needs to go down 1 floor to reach Chefina's room.

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    x, y = 0, 0
    if a % 10 == 0:
        x = a // 10
    else:
        x = (a // 10) + 1
    if b % 10 == 0:
        y = b // 10
    else:
        y = (b // 10) + 1
    print(abs(x-y))
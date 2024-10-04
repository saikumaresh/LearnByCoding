# Design Hashmap

# https://unstop.com/code/challenge-assessment/250158?moduleId=445

# Problem Statement

# Bob, in a fit of anger, vowed to avoid using built-in libraries after an argument with a programming language developer. 
# He's attempting to create his own functions and data structures but got stuck while implementing a HashMap to map unique integer keys to integer values.

# He needs help to perform three basic operations:

# 1. Insert: Add or update a (key, value) pair.
# 2. Get: Print the value for a given key, or -1 if the key doesn't exist.
# 3. Delete: Remove a key and its corresponding value if present.

# Let's assist Bob in building his own HashMap without relying on any pre-existing hash table libraries.

# Input Format
# The first line of the input contains n, the number of queries.
# Each of the next n lines starts with integer t, the type of query.
# For type = 1, the line further contains 2 integers denoting the key and its corresponding value to be inserted.
# For type = 2, the line further contains a single integer denoting the key whose value is to be printed.
# For type = 3, the line further contains a single integer denoting the key that is to be deleted.

# Output Format
# For queries of type 2, print a single integer – value corresponding to the given key.

# Constraints
# 1 <= n <= 104
# 0 <= key, value <= 109

# All the queries are orderly dependent.

# There will be at least one type 2 query.

# In type 3 queries, it is guaranteed that the key given is present in the map at the moment.

# Sample Testcase 0

# Testcase Input
# 8
# 1 1 1
# 1 2 2
# 2 1
# 2 3
# 1 2 1
# 2 2
# 3 2
# 2 2

# Testcase Output
# 1
# -1
# 1
# -1

# Explanation
# For query 1, we insert (1, 1). Our map is now [(1, 1)]
# For query 2, we insert (2, 2). Our map is now [(1, 1), (2, 2)]
# For query 3, we print value corresponding to key 1, i.e., 1
# For query 4, we do not have the key 3 in our map, hence we print -1
# For query 5, we update the value corresponding to key 2 to 1. Out map now is [(1, 1), (2, 1)]
# For query 6, we print the value corresponding to key 2, i.e., 1
# For query 7, we delete the key 2 from the map. Out map now is [(1, 1)]
# For query 8. we do not have the key 2 in our map anymore, hence we print -1


# Sample Testcase 1

# Testcase Input
# 9
# 1 4 2
# 1 25 6
# 2 4
# 1 4 8
# 2 25
# 3 25
# 2 25
# 1 25 1
# 2 25

# Testcase Output
# 2
# 6
# -1
# 1

# Explanation
# For query 1, we insert (4, 2). Our map is now [(4, 2)]
# For query 2, we insert (25, 6). Our map is now [(4, 2), (25, 6)]
# For query 3, we print value corresponding to key 4, i.e., 2
# For query 4, we update the value corresponding to key 4 to 8. Out map now is [(4, 8), (25, 6)]
# For query 5, we print the value corresponding to key 25, i.e., 6
# For query 6, we delete the key 25 from the map. Out map now is [(4, 8)]
# For query 7, we do not have the key 25 in our map anymore, hence we print -1
# For query 8. we insert (25, 1). Our map is now [(4, 8), (25, 1)]
# For query 9, we print the value corresponding to key 25, i.e., 1

class hashmap:
    def __init__(self):
        self.myhash = []

    def insert(self, key, value):
        for i, (k, v) in enumerate(self.myhash):
            if k == key:
                # Update existing key with the new value.
                self.myhash[i] = (key, value)
                return
        # If key doesn't exist, add a new (key, value) pair.
        self.myhash.append((key, value))

    def get(self, key):
        # Search for the key in the map.
        for k, v in self.myhash:
            if k == key:
                return v
        # If key is not found, return -1.
        return -1

    def delete(self, key):
        # Find the key and remove it.
        for i, (k, v) in enumerate(self.myhash):
            if key == k:
                self.myhash.pop(i)
                return


if __name__ == "__main__":
    hashmap = hashmap()
    n = int(input())  # Number of queries.

    for _ in range(n):
        query = list(map(int, input().split()))
        t = query[0]

        if t == 1:
            # Insert operation (key, value).
            key, value = query[1], query[2]
            hashmap.insert(key, value)
        elif t == 2:
            # Get operation (key).
            key = query[1]
            print(hashmap.get(key))
        elif t == 3:
            # Delete operation (key).
            key = query[1]
            hashmap.delete(key)

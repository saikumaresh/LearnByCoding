import os

# Define the folder structure
folders = [
    "Python",
    "SQL",
    "Time_Complexity",
    "Data_Structures/Arrays_and_Strings",
    "Data_Structures/Linked_Lists",
    "Data_Structures/Stacks_and_Queues",
    "Data_Structures/Trees",
    "Data_Structures/Heaps_and_Priority_Queues",
    "Data_Structures/Graphs",
    "Data_Structures/Hashing",
    "Data_Structures/Advanced_Data_Structures",
    "Data_Structures/Strings_and_Pattern_Matching",
    "Data_Structures/Bit_Manipulation",
    "Algorithms/Sorting_and_Searching",
    "Algorithms/Recursion_and_Backtracking",
    "Algorithms/Dynamic_Programming",
    "Algorithms/Greedy_Algorithms",
    "Algorithms/Divide_and_Conquer",
    "Algorithms/Graph_Algorithms",
    "Algorithms/Mathematical_Algorithms",
    "Algorithms/Number_Theory",
    "Algorithms/Two_Pointer_and_Sliding_Window",
    "Miscellaneous"
]

# Create .gitkeep files in each folder
for folder in folders:
    os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
    with open(os.path.join(folder, '.gitkeep'), 'w') as f:
        f.write('')  # Create an empty .gitkeep file

print(".gitkeep files created successfully!")

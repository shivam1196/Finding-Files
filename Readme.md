# PROBLEM 2
## Finding Files
In this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with suffix for example ".c"
<br>
### In this problem I have used -
1. Array -To store path of all the items of current Directory that ends with provided suffix
2. Recursion-To search for file in each sub-directory where each sub-directory is treated as a
sub problem.


### Algorithm:
1. Initialise an array that stores path of all the items in current directory that ends with provided
suffix.
2. For each item in current directory, if it ends with provided suffix then add it to array else if it
is not a file then recursively call the function with subdirectory.


### Time Complexity Analysis:
• Depends upon Maximum number of sub-directory in any directory(B-branching factor of
tree) and depth of subdirectories(D).
• Time Complexity= B*D


### Space Complexity Analysis:
• Space Complexity=B*D

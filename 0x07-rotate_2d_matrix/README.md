# 0x07-rotate_2d_matrix
To solve the problem of rotating an 𝑛 × 𝑛
n×n is a 2D matrix 90 degrees clockwise in place, we'll follow a step-by-step approach. Here's the detailed plan:

Transpose the matrix: Convert all rows to columns.
Reverse each row: After transposing, reverse the elements in each row to get the desired 90-degree rotation.
Pseudocode
Transpose the matrix

Loop through each element in the upper triangle of the matrix (excluding the diagonal).
Swap each element with its corresponding element on the other side of the diagonal.
Reverse each row

Loop through each row and reverse the elements.
---
Explanation
Transposing the matrix:

We loop through each element in the upper triangle of the matrix (excluding the diagonal) and swap it with its counterpart.
This transforms rows into columns.
Reversing each row:

After transposing, each row is reversed to achieve the 90-degree clockwise rotation.

### Test file:
Name a file 0-main.py and put the following code in it: First line with the shaebang #!/usr/bin/python3 then
```
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

### Ensure both files are executable:
Run the following to make them executable: 

```
chmod +x 0-rotate_2d_matrix.py
chmod +x main_0.py
```

### Run the test file
open your terminal and go to the directory that has the code and run: 
```
./main_0.py
```

Output should be: 
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

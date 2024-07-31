# 0x09-island_perimeter
Let's break down the task step-by-step to understand the requirements and plan our solution before implementing it.

### Requirements:
1. We have a 2D grid represented by a list of lists where:
0 represents water.
2. 1 represents land.
3. We need to calculate the perimeter of the island, which is formed by contiguous 1s connected horizontally or vertically.
4. The grid is surrounded by water and does not contain any lakes.
5. There is only one island.

### Plan
Iterate through each cell in the grid.
For each land cell (1), check its four neighbors (top, bottom, left, right).
If a neighbor is water (0) or out of the grid bounds, that contributes to the perimeter.
Sum up all contributions to get the total perimeter.

#### pseudocode: 

```
initialize perimeter to 0
for each row in the grid:
    for each cell in the row:
        if the cell is land (1):
            if the cell above is water or out of bounds:
                increment perimeter
            if the cell below is water or out of bounds:
                increment perimeter
            if the cell to the left is water or out of bounds:
                increment perimeter
            if the cell to the right is water or out of bounds:
                increment perimeter
return perimeter

```
---
## Explanation
The function iterates through each cell in the grid.
For each land cell (1), it checks the four possible neighboring cells.
If the neighbor is water (0) or out of the grid bounds, it contributes to the perimeter.
The final perimeter is returned after checking all cells.
### Suggestions for Next Steps
a. Add unit tests to ensure the function works for various grid configurations.
b. Optimize the function by reducing redundant boundary checks.

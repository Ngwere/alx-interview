# 0x09. Island Perimeter

Calculating the perimeter of an island

# Algorithm: Island Perimeter

##  Input:
- 2D grid, represented as a list of lists, where 0 represents water and 1 represents land

## Output:
- The perimeter of the island in the grid

## Steps:
1. Initialize a variable 'perimeter' to 0.
2. Iterate through each cell in the grid:
   a. If the current cell is land (value is 1):
      i. Initialize a variable 'neighboring_land' to 0.
      ii. Check the cells to the north, south, east, and west of the current cell:
          - If a neighboring cell is land (value is 1), increment 'neighboring_land'.
      iii. Increment 'perimeter' by 4 - 'neighboring_land'.
3. Return the final value of 'perimeter'.

## Time Complexity:
O(m*n), where m is the number of rows and n is the number of columns in the grid, as we need to visit each cell in the grid.

## Space Complexity:
O(1), as we only use a constant amount of extra space to store the 'perimeter' and 'neighboring_land' variables.

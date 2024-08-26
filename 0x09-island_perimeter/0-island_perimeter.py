#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a 2D grid.

    Args:
        grid (List[List[int]]): A 2D grid represented as a list of lists, where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island in the grid.

    Notes:
        - The grid is assumed to be rectangular, with each row having the same number of columns.
        - The grid can be of any size, as long as it is a valid 2D list.
        - If there is no island (no land cells) in the grid, the function will return 0.
        - If there are multiple islands in the grid, the function will return the perimeter of the largest island.

    Examples:
        >>> island_perimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]])
        16
        >>> island_perimeter([[1]])
        4
        >>> island_perimeter([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
        0
        >>> island_perimeter([[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]])
        16
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                neighboring_land = sum(
                    grid[ni][nj] == 1
                    for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0])
                )
                perimeter += 4 - neighboring_land
    return perimeter

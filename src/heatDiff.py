# Name: Venkata Vadrevu
# FSU id: vv18d

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import time


def distribute_heat(old_grid):
    new_grid = np.copy(old_grid)
    for i in range(1,len(new_grid) - 1):
        for j in range(1,len(grid) - 1):
            new_grid[i, j] = 0.25*(old_grid[i - 1, j] + old_grid[i + 1, j] + old_grid[i, j - 1] + old_grid[i, j+1])
    return new_grid


def equals(old_grid, new_grid):
    for i in range(1, len(old_grid) - 1):
        for j in range(1, len(old_grid) - 1):
            if old_grid[i, j] != new_grid[i, j]:
                return False
    return True


def plot_grid(grid):
    fig, ax = plt.subplots()
    y = np.array([[_ for __ in range(len(grid))] for _ in range(len(grid))])
    x = np.array([[__ for __ in range(len(grid))] for _ in range(len(grid))])
    C = grid
    cmap = col.ListedColormap(['darkblue', 'blue', 'aqua', 'lawngreen', 'yellow', 'orange', 'red', 'darkred'])
    ax.scatter(x, y, c=C, cmap = cmap)
    plt.show()


if __name__ == "__main__":
    # start time
    start = time.time()

    # get the temperature from the user
    temp = int(input("Enter the temperature: "))

    # laminar metal
    # created halo cells
    grid = np.array([[temp * 1.00 if i == 0 else 0.00 for i in range(temp + 2)] for j in range(temp + 2)])

    num_iter = 0
    MAX_ITER = 3000
    while num_iter < MAX_ITER:
        print(num_iter)
        old_grid = np.copy(grid)
        grid = distribute_heat(old_grid)
        if equals(old_grid, grid):
            break
        num_iter += 1

    show_grid = np.array([[grid[i][j] for j in range(1, len(grid) - 1)] for i in range(1, len(grid) - 1)])


    #end time
    end = time.time()

    time_taken = end - start
    print("Time taken ", time_taken, "seconds")

    plot_grid(show_grid)


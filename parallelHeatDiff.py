# Name: Venkata Vadrevu
# FSU id: vv18d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import time
import multiprocessing as mp
import os


def distribute_heat_col(y, old_grid):
    result = []
    for x in range(1, len(old_grid) - 1):
        result.append(0.25*(old_grid[x - 1, y] + old_grid[x + 1, y] + old_grid[x, y - 1] + old_grid[x, y + 1]))
    return y,result


def equals(old_grid, grid):
    for i in range(len(old_grid)):
        for j in range(len(old_grid)):
            if old_grid[i, j] != grid[i, j]:
                return False
    return True


def main():

    # get the temperature from the user
    temp = int(input("Enter the temperature: "))

    # laminar metal
    # created halo cells
    grid = np.array([[temp * 1.00 if i == 0 else 0.00 for i in range(temp + 2)] for _ in range(temp + 2)])

    num_iter = 0
    MAX_ITER = 3000
    num_cores = os.cpu_count()

    pool = mp.Pool(processes=num_cores)

    while num_iter < MAX_ITER:
        old_grid = np.copy(grid)
        result = [pool.apply_async(distribute_heat_col, args=(i,old_grid)) for i in range(1, temp+1)]
        for p in result:
            y, arr = p.get()
            for i in range(1, temp+1):
                grid[i, y] = arr[i - 1]

        if equals(grid, old_grid):
            break
        else:
            num_iter += 1

    pool.close()

    return grid


def plot_grid(grid):
    fig, ax = plt.subplots()
    y = np.array([[_ for __ in range(len(grid))] for _ in range(len(grid))])
    x = np.array([[__ for __ in range(len(grid))] for _ in range(len(grid))])
    cmap = col.ListedColormap(['darkblue', 'blue', 'aqua', 'lawngreen', 'yellow', 'orange', 'red', 'darkred'])
    ax.scatter(x,y,c=grid, cmap=cmap)
    plt.show()


if __name__ == "__main__":
    # start time
    start = time.time()
    grid = main()
    end = time.time()
    print("Time taken ", end - start, "seconds")

    show_grid = np.array([[grid[i, j] for j in range(1, len(grid) - 1)] for i in range(1, len(grid) - 1)])
    # Plot the grid
    plot_grid(show_grid)
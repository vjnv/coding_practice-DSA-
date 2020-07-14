def isSafe(x, y, n, maze):
    if 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
        return True
    return False


def solveUtil(x, y, n, sol, maze):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if isSafe(x, y, n, maze):
        sol[x][y] = 1
        if solveUtil(x + 1, y, n, sol, maze):
            return True
        if solveUtil(x, y + 1, n, sol, maze):
            return True
        sol[x][y] = 0
        return False


def solve_rat_in_maze(maze):
    n = len(maze)
    sol = [[0 for i in range(n)] for j in range(n)]
    if solveUtil(0, 0, n, sol, maze) is False:
        return "Solution doesn't exists"
    print(sol)


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
solve_rat_in_maze(maze)

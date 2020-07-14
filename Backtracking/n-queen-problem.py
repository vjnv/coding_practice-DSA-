def isSafe(row, col, sol, n):
    for i in range(col):
        if sol[row][i] == 1:
            return False
    for i in range(1, min(row, col) + 1):
        if sol[row - i][col - i] == 1:
            return False
    for i in range(1, min(n - row - 1, col) + 1):
        if sol[row + i][col - i] == 1:
            return False
    return True


def solveUtil(col, n, sol):
    if col >= n:
        return True
    for row in range(n):
        if isSafe(row, col, sol, n):
            sol[row][col] = 1
            if solveUtil(col + 1, n, sol):
                return True
            sol[row][col] = 0
    return False


def solve(n):
    sol = [[0 for i in range(n)] for j in range(n)]
    if solveUtil(0, n, sol) is False:
        print("Solution doesn't exists!!")
        return
    print(sol)


for n in range(10):
    solve(n)


# output:
# []
# [[1]]
# Solution doesn't exists!!
# Solution doesn't exists!!
# [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
# [[1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0]]
# [[0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0]]
# [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0]]
# [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0]]
# [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0]]

import math


def distribute(candies, n):
    no_of_rounds = (-1 + int(math.sqrt(1 + 8 * candies))) // (2 * n)
    result = [0] * n

    if no_of_rounds>=1:
        for i in range(n):
            result[i] = (i + 1) * no_of_rounds + (no_of_rounds * (no_of_rounds - 1) * n) // 2
            candies -= result[i]
    for i in range(n):
        if candies >= (no_of_rounds) * n + i + 1:
            result[i] += no_of_rounds * n + i + 1
            candies -= (no_of_rounds) * n + i + 1
        else:
            result[i] += candies
            candies -= candies
            break
    return result


testcase = [[7, 4],
            [10, 3],
            [50,5],
            [11,4]]
for test in testcase:
    answer = distribute(test[0], test[1])
    print(answer)

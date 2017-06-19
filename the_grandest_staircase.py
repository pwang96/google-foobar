# The Grandest Staircase


def answer(n):
    # your code here
    if n == 3 or n == 4:
        return 1
    p = [[0 for _ in range(201)] for __ in range(201)]
    p[1][1] = 1
    p[2][2] = 1

    for w in range(3, n+1):
        for m in range(1, w+1):
            if w - m == 0:
                p[w][m] = 1 + p[w][m-1]

            elif w - m < m:
                p[w][m] = p[w-m][w-m] + p[w][m-1]
            elif w - m == m:
                p[w][m] = p[m][m-1] + p[w][m-1]
            elif w - m > m:
                p[w][m] = p[w-m][m-1] + p[w][m-1]

    return p[n][n] - 1

print(answer(6))
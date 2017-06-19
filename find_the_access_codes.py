# Find the Access Codes


def answer(l):
    d = [0] * len(l)
    cnt = 0

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                d[j] += 1

    for i in range(len(l) - 1, 1, -1):
        for j in range(i - 1, 0, -1):
            if l[i] % l[j] == 0:
                cnt += d[j]

    return cnt


l = [1, 1, 1]
print(answer(l))
# Bomb, Baby!


def answer(M, F):
    # your code here
    m = int(M)
    f = int(F)

    cnt = 0
    while m != f and m > 0 and f > 0:
        if m > f:
            cnt += (m // f)
            m -= f * (m // f)

        else:
            cnt += (f // m)
            f -= m * (f // m)

    if (m == 0 and f != 1) or (f == 0 and m != 1):
        return "impossible"
    return str(cnt - 1)


M, M2, M3, M4, M5 = '4', '2', '6,', '2234823948731', '2'
F, F2, F3, F4, F5 = '7', '3', '10000', '2234823948732', '4'

print(answer(M5, F5))

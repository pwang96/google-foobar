# Markov Chain
from fractions import Fraction, gcd


def lcm(lst):
    if len(lst) == 2:
        return lst[0] * lst[1]//gcd(lst[0], lst[1])
    else:
        tmp = lcm([lst[0], lst[1]])
        return lcm([tmp] + lst[2:])


def matrix_subtract(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] -= m2[i][j]
    return m1


def create_identity(size):
    return [[1 if i == j else 0 for i in range(size)] for j in range(size)]


def matrix_mult(m1, m2):
    res = [[0 for __ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 1:
        return [[1/m[0][0]]]
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def answer(m):
    h = len(m)
    if h == 1:
        return [1,1]
    if h == 2:
        return [1, 1]
    w = len(m[0])
    terminal_rows = []
    for row in range(h):
        if all(_ == 0 for _ in m[row]):
            m[row][row] = 1
            terminal_rows.append(row)
    remaining = list(set(range(h)) - set(terminal_rows))

    l = len(remaining)
    M = []
    # TODO
    # for row in terminal_rows:
    #     M.append(m[row])
    # for row in remaining:
    #     M.append(m[row])
    # for row in range(h):
    #     M[row] = M[row][l:] + M[row][:l]
    ordered = terminal_rows + remaining
    for row in terminal_rows:
        M.append([])
        for col in ordered:
            M[-1] += [m[row][col]]

    for row in remaining:
        M.append([])
        for col in ordered:
            M[-1] += [m[row][col]]

    # transform M into rows of fractions
    for row in range(h):
        row_sum = sum(M[row])
        if row_sum != 1:
            for col in range(w):
                if M[row][col]:
                    M[row][col] = Fraction(M[row][col], row_sum)

    r = []
    q = []
    for i in range(len(remaining))[::-1]:
        r.append([M[h - 1 - i][j] for j in range(len(terminal_rows))])
        q.append([M[h - 1 - i][j] for j in range(w - len(remaining), w)])

    print(M)

    i = create_identity(len(q))
    tmp = matrix_subtract(i, q)
    f = getMatrixInverse(tmp)
    for _ in range(len(f)):
        for _1 in range(len(f[0])):
            f[_][_1] = Fraction(f[_][_1]).limit_denominator(2**31)
    fr = matrix_mult(f, r)
    ans = [Fraction(x).limit_denominator(2**31) for x in fr[0]]

    numerators = []
    denominators = []
    for f in ans:
        numerators.append(f.numerator)
        denominators.append(f.denominator)
    common_denominator = lcm(denominators)

    return [int(numerators[i] * (common_denominator/denominators[i])) for i in range(len(numerators))] +\
           [common_denominator]


m = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
m2 = [
    [0, 1],
    [0, 0]
]
m3 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 3, 4, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
m4 = [
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 4, 0, 0, 3, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
# [[1, 0, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 1, 0],
#  [.5, 0, 0, 0, .5, 0]]
print(answer(m1))
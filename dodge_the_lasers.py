# Escape the Lasers
from math import sqrt
import decimal
from decimal import Decimal


def answer(str_n):
    # your code here
    n = int(str_n)
    decimal.getcontext().prec = 1000
    beta = Decimal(2) ** Decimal(0.5) - Decimal(1)

    def helper(n):
        if n == 0:
            return 0
        nprime = int(beta * n)

        return int((n * nprime) + (n * (n + 1) / 2) - (nprime * (nprime + 1) / 2) - helper(nprime))

    return str(helper(n))


print(answer(str(10**100)))
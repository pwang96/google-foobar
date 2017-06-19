# Free the Bunny Prisoners
from itertools import combinations


def answer(num_buns, num_required):
    # your code here
    ans = []

    combos = list(combinations(range(num_buns), num_required))
    bun = len(combos) * num_required
    num_remaining = num_buns - num_required + 1

    combo_remaining = list(combinations(range(num_buns), num_remaining))

    for i in range(num_buns):
        ans.append([])

    for i in range(bun // num_remaining):
        for j in combo_remaining[i]:
            ans[j].append(i)

    return ans


print(answer(5,3))
def clear_highest_bit(x):
    mask = x

    mask |= mask >> 1
    mask |= mask >> 2
    mask |= mask >> 4
    mask |= mask >> 8
    mask |= mask >> 16

    mask >>= 1

    return x & mask, x.bit_length() - 1


def answer(h, q):
    # your code here
    ans = []
    leftnodes = [2 ** _ - 1 for _ in range(1, h + 1)]
    leftnodes2 = [2 ** _ - 2 for _ in range(1, h + 1)]
    for element in q:
        if element == 2 ** h - 1:
            ans.append(-1)
        elif element in leftnodes:
            ans.append(element * 2 + 1)
        elif element in leftnodes2:
            ans.append(element + 1)
        else:
            count = 0
            while ((element + 1) & element) != 0 and ((element + 2) & (element + 1)) != 0:
                tmp, pos = clear_highest_bit(element)
                tmp += 1
                count += element - tmp
                element = tmp
                if ((element + 1) & element) == 0:
                    element = element * 2 + 1
                    break
                elif ((element + 1) & (element + 2)) == 0:
                    element += 1
                    break
            ans.append(element + count)
    return ans

print(answer(5, [30]))
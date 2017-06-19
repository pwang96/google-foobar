def answer(pegs):
    maximum = pegs[1] - pegs[0] - 1
    for x in range(1, maximum):

        gear_sizes = [x]
        for peg in range(1, len(pegs)):
            gear_sizes.append(pegs[peg] - (pegs[peg-1] + gear_sizes[-1]))

        if any(d <= 0 for d in gear_sizes):
            continue

        # see if we got an exact 2/1 match
        if x == 2 * gear_sizes[-1]:
            return [x, 1]

        # test if we have a ratio that works with 3 as the denominator
        if x+1 == 2 * gear_sizes[-1]:
            return [(x * 3) + 1, 3]
        if x+2 == 2 * gear_sizes[-1]:
            return [(x * 3) + 2, 3]

    return [-1, -1]


print(answer([4, 30, 50]))
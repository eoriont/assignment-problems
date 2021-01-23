import timeit


def is_valid(s, n):
    vals = [s for s in sum(s, []) if s is not None]
    if len(set(vals)) != len(vals):
        return False
    arrs = s \
        + [list(arr) for arr in zip(*s)] \
        + [[s[i][i] for i in range(len(s))],
           [s[i][len(s)-i-1] for i in range(len(s))]]
    return all(sum(r) == n for r in arrs if None not in r)


def gen_magic_square():
    for x1 in range(1, 10):
        for x2 in range(1, 10):
            for x3 in range(1, 10):
                for x4 in range(1, 10):
                    for x5 in range(1, 10):
                        for x6 in range(1, 10):
                            for x7 in range(1, 10):
                                for x8 in range(1, 10):
                                    for x9 in range(1, 10):
                                        square = [[x1, x2, x3], [
                                            x4, x5, x6], [x7, x8, x9]]
                                        if is_valid(square, 15):
                                            print(square)
                                            return square


# timeit.timeit('gen_magic_square()', number=1)
gen_magic_square()

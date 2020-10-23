
def arr_to_square(arr):
    return [arr[i:i+3] for i in range(0, 9, 3)]


def is_valid(s, n):
    vals = [i for r in s for i in r if i]
    if len(set(vals)) < len(vals):
        return False
    arrs = s \
        + [list(arr) for arr in zip(*s)] \
        + [[s[i][i] for i in range(len(s))],
           [s[i][len(s)-i-1] for i in range(len(s))]]
    return all(sum(r) == n for r in arrs if None not in r)


def get_magic_const(n):
    return n*(n**2+1)/2


arr1 = [[1, 2, None],
        [None, 3, None],
        [None, None, None]]
print(is_valid(arr1, 15))
# True    (because no rows, columns, or diagonals are completely filled in)

arr2 = [[1, 2, None],
        [None, 3, None],
        [None, None, 4]]
print(is_valid(arr2, 15))
# False   (because a diagonal is filled in and it doesn't sum to 15)

arr3 = [[1, 2, None],
        [None, 3, None],
        [5, 6, 4]]
print(is_valid(arr3, 15))
# False   (because a diagonal is filled in and it doesn't sum to 15)
#         (it doesn't matter that the bottom row does sum to 15)

arr4 = [[None, None, None],
        [None, 3, None],
        [5, 6, 4]]
print(is_valid(arr4, 15))
# True   (because there is one row that's filled in and it sums to 15)


def gen_magic_square(size):
    num = get_magic_const(size)
    square = [None for i in range(size**2)]
    index = 0
    while None in square or not is_valid(arr_to_square(square), num):
        if square[index] == None:
            square[index] = 0
        square[index] += 1
        if square[index] >= len(square)+1:
            square[index] = None
            index -= 1
            continue
        if square.count(square[index]) > 1:
            continue
        if is_valid(arr_to_square(square), num):
            index += 1
    return arr_to_square(square)


# print(arr_to_square([0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(gen_magic_square(4))

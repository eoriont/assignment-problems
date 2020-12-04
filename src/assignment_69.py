def arr_to_square(arr):
    return [arr[i:i+6] for i in range(0, len(arr), 6)]


# def is_valid(s, n):
#     vals = [i for r in s for i in r if i]
#     if len(set(vals)) < len(vals):
#         return False
#     arrs = s \
#         + [list(arr) for arr in zip(*s)] \
#         + [[s[i][i] for i in range(len(s))],
#            [s[i][len(s)-i-1] for i in range(len(s))]]
#     return all(sum(r) == n for r in arrs if None not in r)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield sum(lst[i:i + n], [])


def is_valid(s):
    arr = s + [list(a) for a in zip(*s)] + \
        sum([list(chunks(i, 2))
             for i in [[x[3*i:(i+1)*3] for x in s] for i in range(2)]], [])
    return all({1, 2, 3, 4, 5, 6} == set(x) for x in arr if None not in x)


def print_square(s):
    print("------------")
    for x in s:
        print(x)
    print("------------")


square = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 2, 1, 3], [3, 1, 6, 5, 2, 4],
          [5, 4, 2, 3, 6, 1], [2, 3, 1, 6, 4, 5], [4, 6, 5, 1, 3, 2]]
# print_square(square)
# print(is_valid(square))


def solve_sudoku(square):
    square = sum(square, [])
    filled_in = [i for i in range(len(square)) if square[i] != None]
    index = 0
    forward = True
    while None in square or not is_valid(arr_to_square(square)):
        if index in filled_in:
            index += 1 if forward else -1
            continue
        if square[index] == None:
            square[index] = 0
        square[index] += 1
        if square[index] >= 7:
            square[index] = None
            index -= 1
            forward = False
            continue
        if is_valid(arr_to_square(square)):
            index += 1
            forward = True
    return arr_to_square(square)


print_square(solve_sudoku([[None, None, 4, None, None, None],
                           [None, None, None, 2, 3, None],
                           [3, None, None, None, 6, None],
                           [None, 6, None, None, None, 2],
                           [None, 2, 1, None, None, None],
                           [None, None, None, 5, None, None]]))

# s = [[2, 3, 4, 1, 5, 6], [1, 5, 6, 2, 3, 4], [3, 1, 2, 4, 6, 5],
#      [4, 6, 5, 3, 1, 2], [5, 2, 1, 6, 4, 3], [6, 4, 3, 5, 2, 1]]
# print(is_valid(s))
# print_square(s)

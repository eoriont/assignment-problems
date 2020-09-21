# Magic Num
num = 15


def is_valid(square):
    rows = all(sum(row) == num for row in square if None not in row)
    square_t = [list(arr) for arr in zip(*square)]
    columns = all(sum(col) == num for col in square_t if None not in col)
    diag1 = [square[i][i] for i in range(len(square))]
    diag1 = num == sum(diag1) if None not in diag1 else True
    diag2 = [square_t[i][len(square_t)-i-1] for i in range(len(square_t))]
    diag2 = num == sum(diag2) if None not in diag2 else True
    return rows and columns and diag1 and diag2


arr1 = [[1, 2, None],
        [None, 3, None],
        [None, None, None]]
print(is_valid(arr1))
# True    (because no rows, columns, or diagonals are completely filled in)

arr2 = [[1, 2, None],
        [None, 3, None],
        [None, None, 4]]
print(is_valid(arr2))
# False   (because a diagonal is filled in and it doesn't sum to 15)

arr3 = [[1, 2, None],
        [None, 3, None],
        [5, 6, 4]]
print(is_valid(arr3))
# False   (because a diagonal is filled in and it doesn't sum to 15)
#         (it doesn't matter that the bottom row does sum to 15)

arr4 = [[None, None, None],
        [None, 3, None],
        [5, 6, 4]]
print(is_valid(arr4))
# True   (because there is one row that's filled in and it sums to 15)

# I know this is stupid but I'm really tired right now
for e1 in range(10):
    for e2 in range(10):
        if e2 in [e1]:
            continue
        for e3 in range(10):
            if e3 in [e1, e2]:
                continue
            for e4 in range(10):
                if e4 in [e1, e2, e3]:
                    continue
                for e5 in range(10):
                    if e5 in [e1, e2, e3, e4]:
                        continue
                    for e6 in range(10):
                        if e6 in [e1, e2, e3, e4, e5]:
                            continue
                        for e7 in range(10):
                            if e7 in [e1, e2, e3, e4, e5, e6]:
                                continue
                            for e8 in range(10):
                                if e8 in [e1, e2, e3, e4, e5, e6, e7]:
                                    continue
                                for e9 in range(10):
                                    if e9 in [e1, e2, e3, e4, e5, e6, e7, e8]:
                                        continue
                                    mat = [[e1, e2, e3], [
                                        e4, e5, e6], [e7, e8, e9]]
                                    if is_valid(mat):
                                        print(mat)

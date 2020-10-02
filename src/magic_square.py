# Magic Num
num = 15


def arr_to_square(arr):
    return [arr[i:i+3] for i in range(0, 9, 3)]


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


square = [None for i in range(9)]
index = 0
while None in square or not is_valid(arr_to_square(square)):
    if square[index] == None:
        square[index] = 0
    square[index] += 1
    if square[index] >= 10:
        square[index] = None
        index -= 1
        continue
    if square.count(square[index]) > 1:
        continue
    if is_valid(arr_to_square(square)):
        index += 1


print(arr_to_square(square))

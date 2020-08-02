# Merge lists
def combine_sorted_lists(arr1, arr2):
    result = []
    i, j = 0, 0
    while len(arr1) > i and len(arr2) > j:
        e1 = arr1[i]
        e2 = arr2[j]
        if e1 < e2:
            result.append(e1)
            i += 1
        else:
            result.append(e2)
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result

# Just call it merge sort...


def divide_and_conquer_sort(x):
    l = len(x)
    if l == 2:
        if x[0] < x[1]:
            return x
        else:
            return x[::-1]
    elif l == 1:
        return x
    x1 = divide_and_conquer_sort(x[:l//2])
    x2 = divide_and_conquer_sort(x[l//2:])
    return combine_sorted_lists(x1, x2)

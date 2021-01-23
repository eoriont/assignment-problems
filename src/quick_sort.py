# Inefficient
def quick_sort2(arr):
    if len(arr) == 0:
        return []
    pivot, l = arr[-1], [[], []]
    for i in arr[:-1]:
        if i > pivot:
            l[0].append(i)
        else:
            l[1].append(i)
    l[0], l[1] = quick_sort(l[0]), quick_sort(l[1])
    return l[1] + [pivot] + l[0]

# Modifies in place


def quick_sort(arr, l=0, r=-1):
    r = len(arr) if r == -1 else r
    if r - l in (0, 1):
        return
    i = l+1
    for x in range(l, r):
        if arr[l] > arr[x]:
            arr[i], arr[x] = arr[x], arr[i]
            i += 1
    arr[i-1], arr[l] = arr[l], arr[i-1]
    quick_sort(arr, l, i)
    quick_sort(arr, i, r)
    return arr


if __name__ == "__main__":
    from otest import do_assert
    do_assert("quick_sort", quick_sort(
        [5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]), [-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10])

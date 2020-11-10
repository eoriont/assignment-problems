
def quick_sort(arr):
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


if __name__ == "__main__":
    from otest import do_assert
    do_assert("quick_sort", quick_sort(
        [5, 8, -1, 9, 10, 3.14, 2, 0, 7, 6]), [-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10])

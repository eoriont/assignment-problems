from otest import do_assert


def binary_search(x, l):
    m = len(l)//2
    return m if x == l[m] else binary_search(x, l[m:] if x > l[m] else l[:m])


do_assert("Binary Search Test", binary_search(
    7, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]), 3)

import sys
sys.path.append("src")
try:
    from combine_sorted_lists import combine_sorted_lists
    from otest import do_assert, cstring
except ImportError as e:
    print(e)

tests = [
    ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]),
    ([-1, 5, 10, 11.23, 14.1], [-801, -40, 0, 3.14, 11.24, 15]),
    ([1], [2]),
    ([], [1]),
]

for test in tests:
    output = combine_sorted_lists(*test)
    expected = sorted(sum(test, []))
    do_assert("combine sorted lists", output, expected)

print(cstring("&6All tests passed!"))

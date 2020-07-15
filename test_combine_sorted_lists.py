from combine_sorted_lists import combine_sorted_lists

tests = [
    ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]),
    ([-1, 5, 10, 11.23, 14.1], [-801, -40, 0, 3.14, 11.24, 15]),
    ([1], [2]),
    ([], [1]),
]

for test in tests:
    output = combine_sorted_lists(*test)
    expected = sorted(sum(test, []))
    assert output == expected, f"Test combine_sorted_lists failed! Expected output: {expected}, but actually got {output}"
    print("Test combine_sorted_lists passed")

print("All tests passed!")

def func(x):
    return x**2 - 5


def bisection_search(bounds):
    mid = sum(bounds)/2
    f = func(mid)
    if round(f, 4) == 0:
        return
    print(f"\nMiddle is {mid}. f({mid}) = {f}.")
    if f < 0:
        print("It is greater than 0 so the guess is too high. We must raise the bounds")
        bisection_search([mid, bounds[1]])
    else:
        print("It is less than 0 so the guess is too low. We must lower the bounds")
        bisection_search([bounds[0], mid])


bisection_search([2, 3])

import math


def calc_standard_normal_probability(a, b):
    return 1/math.sqrt(2*math.pi) * sum(math.exp(-0.5 * (x*0.001)**2)*0.001 for x in range(a*1000, b*1000))


# The assignment said to print, not to test!
print(calc_standard_normal_probability(-1, 1))
print(calc_standard_normal_probability(-2, 2))
print(calc_standard_normal_probability(-3, 3))

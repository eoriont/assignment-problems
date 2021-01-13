import math
import matplotlib.pyplot as plt


def calc_standard_normal_probability(a, b, n, rule):
    step_size, inv_ss = (b-a)/n, n//(b-a)
    def f(x): return math.exp(-0.5 * x**2)
    if rule == "left endpoint":
        sum1 = sum(f(x*step_size) for x in range(a*inv_ss, b*inv_ss))
    elif rule == "right endpoint":
        sum1 = sum(f(x*step_size) for x in range(a*inv_ss+1, b*inv_ss+1))
    elif rule == "midpoint":
        sum1 = sum(f((2*x+1)/2*step_size) for x in range(a*inv_ss, b*inv_ss+1))
    elif rule == "trapezoidal":
        sum1 = sum(f(x*step_size) for x in range(a*inv_ss+1, b*inv_ss)) + \
            (f(a) + f(b))/2
    elif rule == "simpson":
        sum1 = (sum((4 if x % 2 == 0 else 2) * f(x*step_size) for x in range(a*inv_ss+1, b*inv_ss)) +
                f(a) + f(b))/3
    return 1/math.sqrt(2*math.pi) * sum1 * step_size


# The assignment said to print, not to test!
# print(calc_standard_normal_probability(-1, 1, 1000, "left endpoint"))
# print(calc_standard_normal_probability(-2, 2, 1000, "left endpoint"))
# print(calc_standard_normal_probability(-3, 3, 1000, "left endpoint"))
y_data = [
    [calc_standard_normal_probability(
        0, 1, n, "left endpoint") for n in range(1, 101)],
    [calc_standard_normal_probability(
        0, 1, n, "right endpoint") for n in range(1, 101)],
    [calc_standard_normal_probability(0, 1, n, "midpoint")
     for n in range(1, 101)],
    [calc_standard_normal_probability(
        0, 1, n, "trapezoidal") for n in range(1, 101)],

]
x_vals = [i for i in range(1, 101)]

colors = ["red", "orange", "black", "green", "blue"]

for y_vals, col in zip(y_data, colors):
    plt.plot(x_vals, y_vals, zorder=1, color=col)

plt.plot(range(1, 101, 2), [calc_standard_normal_probability(0, 1, n, "simpson")
                            for n in range(1, 101, 2)], color=colors[-1])
plt.show()

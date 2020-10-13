from euler_estimator import EulerEstimator
import math
import matplotlib.pyplot as plt


def dn(t, x):
    return (0.01*(10-x[0])*(1-x[1])) / \
        (math.exp(10-x[0])-1) - x[1] * 0.125 * math.exp(-x[0]/80)


def dm(t, x):
    return ((0.1*(25-x[0])*(1-x[2]))/(math.exp(0.1*(25-x[0]))-1) - 4*math.exp(-x[0]/18)*x[2])


def dh(t, x):
    return (0.07*math.exp(-x[0]/20)*(1-x[3])) - x[3]/(math.exp(0.1*(30-x[0]))+1)


def s_t(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or \
            30 <= t <= 40 or 50 <= t <= 51 or \
            53 <= t <= 54 or 56 <= t <= 57 or \
            59 <= t <= 60 or 62 <= t <= 63 or \
            65 <= t <= 66:
        return 150
    return 0


def dV(t, x):
    return s_t(t) - 120*(x[2]**3)*x[3]*(x[0]-115)-36*(x[1]**4)*(x[0]+12)-0.3*(x[0]-10.6)


derivatives = [dV, dn, dm, dh]

# h(0)
x = 0.07 * (math.e**3 + 1)
h_0 = x/(x+1)

# n(0)
n_0 = 1/(1.25*(math.e-1)+1)

# m(0)
m_0 = 2.5/(2.5+4*(math.e**2.5 - 1))

# V(0)
V_0 = 0

starting_point = (0, (V_0, n_0, m_0, h_0))
print(starting_point)

estimator = EulerEstimator(derivatives, starting_point)
plt.plot([n/2 for n in range(160)], [s_t(n/2) for n in range(160)], zorder=1)

estimator.plot([0, 80], step_size=0.01,
               filename="epic_assignment_52_plot.png")

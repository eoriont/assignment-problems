from euler_estimator import EulerEstimator
import math
import matplotlib.pyplot as plt


def a_n(t, x):
    return 0.01*(10-x[0])/(math.exp(0.1*(10-x[0]))-1)


def b_n(t, x):
    return 0.125*math.exp(-x[0]/80)


def a_m(t, x):
    return 0.1*(25-x[0])/(math.exp(0.1*(25-x[0]))-1)


def b_m(t, x):
    return 4*math.exp(-x[0]/18)


def a_h(t, x):
    return 0.07 * math.exp(-x[0]/20)


def b_h(t, x):
    return 1/(math.exp(0.1*(30-x[0]))+1)


def dn(t, x):
    return a_n(t, x)*(1 - x[1]) - b_n(t, x)*x[1]


def dm(t, x):
    return a_m(t, x)*(1 - x[2]) - b_m(t, x)*x[2]


def dh(t, x):
    return a_h(t, x)*(1 - x[3]) - b_h(t, x)*x[3]


C = 1
Vna = 115
Vk = -12
VL = 10.6
_gna = 120
_gk = 36
_gl = 0.3


def INa(t, x):
    return gna(t, x)*(x[0]-Vna)


def gna(t, x):
    return _gna * x[2]**3 * x[3]


def Ik(t, x):
    return gk(t, x)*(x[0]-Vk)


def gk(t, x):
    return _gk * x[1]**4


def IL(t, x):
    return gl(t, x)*(x[0]-VL)


def gl(t, x):
    return _gl


def dV(t, x):
    return 1/C * (s_t(t) - INa(t, x) - Ik(t, x) - IL(t, x))


def s_t(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or \
            30 <= t <= 40 or 50 <= t <= 51 or \
            53 <= t <= 54 or 56 <= t <= 57 or \
            59 <= t <= 60 or 62 <= t <= 63 or \
            65 <= t <= 66:
        return 150
    return 0


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

estimator = EulerEstimator(derivatives, starting_point)
plt.plot([n/2 for n in range(160)], [s_t(n/2) for n in range(160)], zorder=1)

estimator.plot([0, 80], step_size=0.02,
               filename="epic_assignment_52_plot.png")

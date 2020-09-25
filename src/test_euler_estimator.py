from euler_estimator import EulerEstimator
from otest import do_assert


def _round(t):
    return tuple(round(x, 5) for x in t)


euler = EulerEstimator(
    derivatives=[
        (lambda t, x: x[0] + 1),
        (lambda t, x: x[0] + x[1]),
        (lambda t, x: 2*x[1])
    ],
    point=(0, (0, 0, 0))
)

do_assert("point", euler.point,
          (0, (0, 0, 0)))
do_assert("calc derivative", euler.calc_derivative_at_point(),
          [1, 0, 0])

euler.step_forward(0.1)
do_assert("step forward", euler.point,
          (0.1, (0.1, 0, 0)))

do_assert("new derivative", euler.calc_derivative_at_point(),
          [1.1, 0.1, 0])
euler.step_forward(-0.5)
do_assert("step forward 2", euler.point,
          (-0.4, (-0.45, -0.05, 0)))

euler.go_to_input(5, step_size=2)

# notes to help you debug:

# point: (-0.4, (-0.45, -0.05, 0))
# derivative: (0.55, -0.5, -0.1)
# deltas: (2, (1.1, -1, -0.2))

# point: (1.6, (0.65, -1.05, -0.2))
# derivative: (1.65, -0.4, -2.1)
# deltas: (2, (3.3, -0.8, 4.2))

# point: (3.6, (3.95, -1.85, 4))
# derivative: (4.95, 2.1, -3.7)
# deltas: (1.4, (9.8, 4.2, -7.4))

do_assert("go to input", euler.point[1],
          (10.88, 1.09, -9.58))

euler.plot([-5, 5], step_size=0.1, filename='plot.png')

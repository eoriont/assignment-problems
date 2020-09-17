from euler_estimator import EulerEstimator
from otest import do_assert


def _round(t):
    return tuple(round(x, 5) for x in t)


euler = EulerEstimator(derivative=(lambda x: x+1),
                       point=(1, 4))

do_assert("euler point", euler.point,
          (1, 4))
do_assert("calc derivative", euler.calc_derivative_at_point(), 2)
# 2     (because the derivative is f'(x)=x+1, so f'(1)=2)

euler.step_forward(0.1)
do_assert("euler point after step forward", euler.point,
          (1.1, 4.2))  # (because 4 + 0.1*2=4.2)

do_assert("derivative after step", euler.calc_derivative_at_point(),
          2.1)
euler.step_forward(-0.5)
do_assert("step forward point 2", _round(euler.point),
          (0.6, 3.15))  # (because 4.2 + -0.5*2.1=3.15)

euler.go_to_input(3, step_size=0.5)

# note: you should move to the x-coordinate of 3
# using a step_size of 0.5, until the final step,
# in which you need to reduce the step_size to hit 3

# the following is provided to help you debug:

# point, derivative, deltas
# (0.6, 3.15), 1.6, (0.5, 0.8)
# (1.1, 3.95), 2.1, (0.5, 1.05)
# (1.6, 5), 2.6, (0.5, 1.3)
# (2.1, 6.3), 3.1, (0.5, 1.55)
# (2.6, 7.85), 3.6, (0.4, 1.44)

do_assert("euler point after go_to_input", _round(euler.point),
          (3, 9.29))

from euler_estimator import EulerEstimator

euler = EulerEstimator(derivative=(lambda x: x+1),
                       point=(1, 4))

euler.plot([-5, 5], step_size=0.1, filename='plot.png')

# generates a plot of the function for x-values in the
# interval [-5,5] separated by a length of step_size

# for this example, the plot should look like the parabola
# y = 0.5x^2 + x + 2.5

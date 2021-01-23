from euler_estimator import EulerEstimator
derivatives = [
    (lambda t, x: 0.6*x[0] - 0.05*x[0]*x[1]),
    (lambda t, x: -0.9*x[1] + 0.02*x[0]*x[1])
]
starting_point = (0, (100, 10))

estimator = EulerEstimator(derivatives, starting_point)

estimator.plot([0, 100], step_size=0.001,
               filename="epic_assignment_48_plot.png")

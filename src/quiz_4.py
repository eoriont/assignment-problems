from euler_estimator import EulerEstimator
derivatives = [
    (lambda t, x: -0.0003*x[0]*x[1]),
    (lambda t, x: 0.0003*x[0]*x[1] - 0.02*x[1] - 0.001 * x[1]),
    (lambda t, x: 0.02*x[1]),
    (lambda t, x: 0.001 * x[1])
]
starting_point = (0, (1000, 1, 0, 0))

estimator = EulerEstimator(derivatives, starting_point)

estimator.plot([0, 365], step_size=0.001,
               filename="quiz_4.png")

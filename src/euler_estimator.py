class EulerEstimator:
    def __init__(self, derivative, point):
        self.point = point
        self.derivative = derivative

    def calc_derivative_at_point(self):
        return self.derivative(self.point[0])

    def step_forward(self, step_size):
        x, y = self.point
        self.point = x+step_size, y + step_size*self.calc_derivative_at_point()

    def go_to_input(self, x_val, step_size):
        while self.point[0] != x_val:
            if abs(self.point[0] - x_val) <= step_size:
                step_size = x_val-self.point[0]
            self.step_forward(step_size)

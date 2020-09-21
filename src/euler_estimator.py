import matplotlib.pyplot as plt


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
        if x_val < self.point[0]:
            step_size *= -1
        while round(self.point[0], 10) != x_val:
            if abs(self.point[0] - x_val) <= step_size:
                step_size = x_val-self.point[0]
            self.step_forward(step_size)
            if self.point[0] < -10:
                break

    def plot(self, r, step_size, filename):
        x_data = [i for i in range(*r)]
        y_data = []
        for x in x_data:
            self.go_to_input(x, step_size)
            y_data.append(self.point[1])
        plt.scatter(x_data, y_data, zorder=2, color='black')
        plt.plot(x_data, y_data, zorder=1)
        plt.savefig(filename)

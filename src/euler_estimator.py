import matplotlib.pyplot as plt


class EulerEstimator:
    def __init__(self, derivative, point):
        self.point = point
        self.derivative = derivative

    def calc_derivative_at_point(self):
        return self.derivative(self.point[0])

    def step_forward(self, step_size):
        x = round(self.point[0]+step_size, 10)
        y = round(self.point[1] + step_size *
                  self.calc_derivative_at_point(), 10)
        self.point = x, y

    def go_to_input(self, x_val, step_size):
        if x_val < self.point[0]:
            step_size *= -1
        while round(self.point[0], 10) != x_val:
            if abs(round(self.point[0] - x_val, 10)) <= step_size:
                step_size = x_val-self.point[0]
            self.step_forward(step_size)

    def plot(self, r, step_size, filename):
        x_data = [round(r[0]+i*step_size, 10)
                  for i in range(int((r[1]-r[0])/step_size))]
        given_index = x_data.index(self.point[0])
        given_point = self.point
        y_data = []
        for x in x_data[:given_index][::-1]:
            self.go_to_input(x, step_size)
            y_data.insert(0, self.point[1])
        self.point = given_point
        for x in x_data[given_index:]:
            self.go_to_input(x, step_size)
            y_data.append(self.point[1])

        print(min(y_data))        plt.plot(x_data, y_data, zorder=1)
        plt.savefig(filename)

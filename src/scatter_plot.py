import matplotlib.pyplot as plt

data = [[2, 13, 'B'], [2, 13, 'B'], [2, 13, 'B'], [2, 13, 'B'], [2, 13, 'B'], [2, 13, 'B'],
        [3, 13, 'B'], [3, 13, 'B'], [3, 13, 'B'], [
            3, 13, 'B'], [3, 13, 'B'], [3, 13, 'B'],
        [2, 12, 'B'], [2, 12, 'B'],
        [3, 12, 'A'], [3, 12, 'A'],
        [3, 11, 'A'], [3, 11, 'A'],
        [3, 11.5, 'A'], [3, 11.5, 'A'],
        [4, 11, 'A'], [4, 11, 'A'],
        [4, 11.5, 'A'], [4, 11.5, 'A'],
        [2, 10.5, 'A'], [2, 10.5, 'A'],
        [3, 10.5, 'B'],
        [4, 10.5, 'A']]

d = {k: [(x[0], x[1]) for x in data if x[2] == k]
     for k in set(list(zip(*data))[2])}

for k, v in d.items():
    plt.scatter(*zip(*v), c='r' if k == 'A' else 'b', s=[v.count(x)*15
                                                         for x in v])

plt.show()

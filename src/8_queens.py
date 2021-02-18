import random


def show_board(locs):
    print(''.join('  '.join((str(locs.index((x, y))) if (x, y) in locations else ".")
                            for y in range(8)) + "\n" for x in range(8)))


def calc_cost(locs):
    cost = []
    for i, (x, y) in enumerate(locs):
        for j, (x1, y1) in enumerate(locs):
            if i == j:
                continue
            if x == x1 or y == y1 or abs((y-y1)/(x-x1)) == 1:
                if (j, i) not in cost:
                    cost.append((i, j))
    return len(cost)


def random_optimizer(n):
    locs = [random.sample([(x, y) for x in range(8)
                           for y in range(8)], 8) for _ in range(n)]
    optimized = min(locs, key=calc_cost)
    return {
        'locations': optimized,
        'cost': calc_cost(optimized)
    }


def is_in_bounds(pos):
    return 0 <= pos.x <= 7 and 0 <= pos.y <= 7


def steepest_descent_optimizer(n):
    optimized = {'cost': 1000}
    translations = [(x, y) for x in range(-1, 2)
                    for y in range(-1, 2) if (x, y) != (0, 0)]
    for i in range(n):
        rand = random_optimizer(100)
        for t in translations:
            for i in range(len(rand['locations'])):
                new_locations = [l if j != i else (
                    l[0]+t[0], l[1]+t[1]) for j, l in enumerate(rand['locations'])]
                cost = calc_cost(new_locations)
                if (cost < optimized['cost']):
                    optimized = {
                        'cost': cost,
                        'locations': new_locations
                    }
    return optimized


locations = [(0, 0), (6, 1), (2, 2), (5, 3), (4, 4), (7, 5), (1, 6), (2, 6)]
show_board(locations)

ns = [10, 50, 100, 500, 1000]

for n in ns:
    print(steepest_descent_optimizer(n))

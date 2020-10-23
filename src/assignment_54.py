
def dist(p1, p2):
    return sum((x-y)**2 for x, y in zip(p1, p2))**0.5


cookies = [[1, 'Shortbread',     0.14,       0.14,      0.28,     0.44],
           [2, 'Shortbread',     0.10,       0.18,      0.28,     0.44],
           [3, 'Shortbread',     0.12,       0.10,      0.33,     0.45],
           [4, 'Shortbread',     0.10,       0.25,      0.25,     0.40],
           [5, 'Sugar',     0.00,       0.10,      0.40,     0.50],
           [6, 'Sugar',     0.00,       0.20,      0.40,     0.40],
           [7, 'Sugar',     0.10,       0.08,      0.35,     0.47],
           [8, 'Sugar',     0.00,       0.05,      0.30,     0.65],
           [9, 'Fortune',     0.20,       0.00,      0.40,     0.40],
           [10, 'Fortune',     0.25,       0.10,      0.30,     0.35],
           [11, 'Fortune',     0.22,       0.15,      0.50,     0.13],
           [12, 'Fortune',     0.15,       0.20,      0.35,     0.30],
           [13, 'Fortune',     0.22,       0.00,      0.40,     0.38]]

cookies = [{'id': x[0], 'type': x[1], 'point': x[2:]} for x in cookies]

new_cookie = [0.1, 0.15, 0.3, 0.45]

# Part A
distances = [{'type': x['type'], 'dist': dist(
    x['point'], new_cookie), 'id': x['id']} for x in cookies]
print(distances)

# Part B
nearest_neigbors = [x for x in sorted(distances, key=lambda x: x['dist'])[:5]]

print(nearest_neigbors)

# Part 2A
nearest_neigbors = [x for x in sorted(distances, key=lambda x: x['dist'])[:13]]

print(nearest_neigbors)

# Part 2B

c = {}

for x in distances:
    if x['type'] not in c:
        c[x['type']] = []
    c[x['type']].append(x)

cookies = {}
for t, cs in c.items():
    print(cs)
    cookies[t] = sum(x['dist'] for x in cs) / len(cs)

print(cookies)

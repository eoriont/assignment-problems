import random


def random_draw(distribution):
    cumulative_distribution = [sum(distribution[:i+1])
                               for i in range(len(distribution))]
    rand_num = random.uniform(0, 1)
    for i, x in enumerate(cumulative_distribution):
        if x > rand_num:
            return i


def random_draw_test(dist):
    nums = {}
    for i in range(1000):
        n = random_draw(dist)
        if n not in nums:
            nums[n] = 0
        nums[n] += 1
    print(nums)


random_draw_test([0.5, 0.5])
random_draw_test([0.25, 0.25, 0.5])
random_draw_test([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])

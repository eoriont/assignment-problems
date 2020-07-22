import random


def probability(num_heads, num_flips):
    possible_outcomes = 2**num_flips
    outcomes_permutation = factorial(
        num_flips) / (factorial(num_flips - num_heads) * factorial(num_heads))
    return outcomes_permutation / possible_outcomes


def monte_carlo_probability(num_heads, num_flips):
    total_trials = 1000
    match_flips = 0
    for _ in range(total_trials):
        trial = [random.randint(0, 1) for _ in range(num_flips)]
        if trial.count(1) == num_heads:
            match_flips += 1

    return match_flips / total_trials


def factorial(num):
    return 1 if num in [0, 1] else factorial(num-1) * num


print("Normal Probability Using Combination")
print(probability(5, 8))
print("Monte Carlo Probability Trials")
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))
print(monte_carlo_probability(5, 8))

import random
import matplotlib.pyplot as plt
plt.style.use("bmh")


def probability(num_heads, num_flips):
    possible_outcomes = 2**num_flips
    outcomes_permutation = factorial(
        num_flips) / (factorial(num_flips - num_heads) * factorial(num_heads))
    return outcomes_permutation / possible_outcomes


def monte_carlo_trials(num_flips, total_trials):
    trials = {}
    for _ in range(total_trials):
        trial = [random.randint(0, 1) for _ in range(num_flips)]
        heads = trial.count(1)
        if heads in trials:
            trials[heads] += 1
        else:
            trials[heads] = 1
    result = {x: y/total_trials for x, y in trials.items()}
    result = dict_to_list(result, num_flips)
    return result


def monte_carlo_probability(num_heads, num_flips):
    return monte_carlo_trials(num_flips, 1000)[num_heads]


def dict_to_list(d, length):
    default_dict = {x: 0 for x in range(length+1)}
    default_dict.update(d)
    return list(zip(*sorted(default_dict.items(), key=lambda x: x[0])))[1]


def factorial(num):
    return 1 if num in [0, 1] else factorial(num-1) * num


def plot_probabilities(probabilities):
    # Graph them
    x_vals = [x for x in range(len(probabilities[0]))]
    for i, probs in enumerate(probabilities):
        line_width = 2.5 if i == 0 else 0.75
        plt.plot(x_vals, probs, linewidth=line_width)

    plt.legend(["True", "MC 1", "MC 2"])
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability")
    plt.title("True Distribution vs Monte Carlo Simulations for 10 Coin Flips")
    plt.show()


if __name__ == "__main__":
    # True Probabilities
    probabilities = [[probability(x, 10) for x in range(11)]]

    # Monte Carlo Probabilities
    probabilities += [monte_carlo_trials(10, 1000) for _ in range(5)]
    print(probabilities)
    plot_probabilities(probabilities)

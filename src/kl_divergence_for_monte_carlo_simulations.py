import math
from coin_flipping import monte_carlo_trials, probability


def kl_divergence(p, q):
    return sum(px*math.log(px/qx) if px > 0 and qx > 0 else 0 for px, qx in zip(p, q))


def main():
    p = [0.2, 0.7, 0.1]
    q = [0.1, 0.8, 0.1]
    divergence = kl_divergence(p, q)
    assert divergence == 0.045157461274823146, "kl_divergence test failed!"
    print("kl_divergence test PASSED!")

    print("Computing KL for MC Simulations...")

    samples = 100
    true_probability = [probability(x, 5) for x in range(6)]
    trials = monte_carlo_trials(5, samples)
    print(f"{samples} samples --> KL Divergence = ",
          kl_divergence(trials, true_probability))

    samples = 1000
    true_probability = [probability(x, 5) for x in range(6)]
    trials = monte_carlo_trials(5, samples)
    print(f"{samples} samples --> KL Divergence = ",
          kl_divergence(trials, true_probability))

    samples = 10000
    true_probability = [probability(x, 5) for x in range(6)]
    trials = monte_carlo_trials(5, samples)
    print(f"{samples} samples --> KL Divergence = ",
          kl_divergence(trials, true_probability))

    # As the number of samples increases, the KL divergence decreases because more samples means the monte carlo estimate
    # is going to be closer to the real probability, and the KL divergence is how far away the estimate is from the true probability.


if __name__ == "__main__":
    main()

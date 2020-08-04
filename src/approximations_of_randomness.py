from coin_flipping import probability
from kl_divergence_for_monte_carlo_simulations import kl_divergence


def main():
    flips = {
        'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
        'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
        'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
        'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
        'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
    }

    trial_flips = 4

    # Split simulations into trials
    trials = {name: simulation.split(" ")
              for name, simulation in flips.items()}

    # Get number of heads for each trial
    trial_heads = {name: [trial.count('H') for trial in coin_flips]
                   for name, coin_flips in trials.items()}

    # Get probability of # of heads for each simulation
    probs = {name: [trial.count(x)/len(trial) for x in range(trial_flips)]
             for name, trial in trial_heads.items()}

    # Calculate the true probability of getting heads
    true_probability = [probability(x, trial_flips)
                        for x in range(trial_flips+1)]

    print("KL Divergence between coin flips")
    for name, probs in probs.items():
        div = kl_divergence(probs, true_probability)
        print(name, ":", div)
	
    print("According to the KL divergence, Justin's coin flipping was the best approximation of true randomness because it was the closest to the true probability.")


if __name__ == "__main__":
    main()

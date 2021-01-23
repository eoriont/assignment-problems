
def calc_probs(trial):
    probabilities = [0, 0, 0, 0]
    trials_to_consider = [0, 0]
    for i in range(len(trial)-1):
        two_flips = trial[i:i+2]
        flips = ['HH', 'HT', 'TH', 'TT']
        probabilities[flips.index(two_flips)] += 1
        trials_to_consider[flips.index(two_flips) // 2] += 1
    return probabilities, trials_to_consider


def print_prob(probs):
    print(f"P(next flip heads | last flip heads): {probs[0]}")
    print(f"P(next flip tails | last flip heads): {probs[1]}")
    print(f"P(next flip heads | last flip tails): {probs[2]}")
    print(f"P(next flip tails | last flip tails): {probs[3]}")


if __name__ == "__main__":
    flips = {
        'George': 'THTH HTHT THTH HHTH THTH TTHT THTH TTTH THTH TTHT THHT HTTH THTH THHT THHT THTH THTH THHT THTH THTH',
        'David': 'TTHH HHTT HHTT TTHH HTHT THTH THTH THTH HTHT HTHT THTH HTHT THHH THTH HHTT HHTT TTTH HHTH HTHH TTTH',
        'Elijah': 'THTT HTHT HTHH HHHT TTHH THHH TTTT HHTT TTTH TTHH HTHT HTHT TTTT HTTT TTTH HTTT TTHH THTH THHH HTHH',
        'Colby': 'HTTH HTHH THTT HHTH TTHT HTTT THHH TTHH HHTT THTH HHTT THTH THHH TTHH THTT HHTH HTTH HTHH TTHT HTTT',
        'Justin': 'THTT HTHT TTTH THHT HTHH TTTH THTH HHTH TTTT HTTH HHTT THHH HHHH THTH HTTH TTHH HTHT HHHT THHT TTTH'
    }
    probs = {}
    for name, trials in flips.items():
        trials = trials.split(" ")
        # List of the 4 probabilities we had to calculate
        probabilities, trials_to_consider = zip(
            *list(calc_probs(trial) for trial in trials))
        probabilities = [sum(x) for x in zip(*probabilities)]
        trials_to_consider = [sum(x) for x in zip(*trials_to_consider)]
        trial = [p / trials_to_consider[i//2]
                 for i, p in enumerate(probabilities)]
        print(f"{name}'s probabilities:")
        print_prob(trial)

    print("Other test probability:")
    dataset = "HHTTHT"
    prob = calc_probs(dataset)
    trial = [p / prob[1][i//2]
             for i, p in enumerate(prob[0])]
    print_prob(trial)

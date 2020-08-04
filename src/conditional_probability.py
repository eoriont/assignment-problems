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
    probabilities = [0, 0, 0, 0]
    for trial in trials:
        for i in range(len(trial)-1):
            two_flips = trial[i:i+2]
            flips = ['HH', 'HT', 'TH', 'TT']
            probabilities[flips.index(two_flips)] += 1
    trials_to_consider = (len(trials[0])-1) * len(trials)
    probs[name] = [p / trials_to_consider for p in probabilities]

for name, trial in probs.items():
    print(f"{name}'s probabilities:")
    print(f"P(next flip heads | last flip heads): {trial[0]}")
    print(f"P(next flip tails | last flip heads): {trial[1]}")
    print(f"P(next flip heads | last flip tails): {trial[2]}")
    print(f"P(next flip tails | last flip tails): {trial[3]}")
